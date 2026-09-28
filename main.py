"""Tkinter front end: type text, pick a language, and hear it spoken."""

import queue
import shutil
import tempfile
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, ttk

from speech import SpeechError, languages, play, synthesize

BG = "#f0f0f0"


class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.langs = languages()
        self.audio = Path(tempfile.gettempdir()) / "text-to-speech-output.mp3"
        self.has_audio = False
        # Worker threads report back through this queue: Tk may only be touched from the thread
        # running its event loop, so the worker never calls into Tk itself.
        self.results: queue.Queue = queue.Queue()

        root.title("Text-to-Speech")
        root.configure(bg=BG, padx=20, pady=20)
        root.resizable(False, False)

        tk.Label(
            root, text="Text-to-Speech Converter", font=("Helvetica", 18, "bold"), bg=BG
        ).pack()
        tk.Label(root, text="Enter your text below:", font=("Helvetica", 12), bg=BG).pack(
            pady=(12, 4)
        )
        self.entry = tk.Text(root, width=50, height=6, font=("Helvetica", 12), wrap="word")
        self.entry.pack()

        row = tk.Frame(root, bg=BG)
        row.pack(pady=10)
        tk.Label(row, text="Language:", bg=BG).pack(side="left")
        self.language = ttk.Combobox(
            row, values=list(self.langs.values()), state="readonly", width=24
        )
        self.language.set(self.langs.get("en", next(iter(self.langs.values()))))
        self.language.pack(side="left", padx=6)

        buttons = tk.Frame(root, bg=BG)
        buttons.pack()
        self.speak_button = tk.Button(buttons, text="Speak", width=10, command=self.speak)
        self.speak_button.pack(side="left", padx=4)
        self.save_button = tk.Button(
            buttons, text="Save MP3…", width=10, command=self.save, state="disabled"
        )
        self.save_button.pack(side="left", padx=4)
        tk.Button(buttons, text="Clear", width=10, command=self.clear).pack(side="left", padx=4)
        tk.Button(buttons, text="Exit", width=10, command=root.destroy).pack(side="left", padx=4)

        self.status = tk.Label(root, text="", font=("Helvetica", 10), bg=BG)
        self.status.pack(pady=(10, 0))

        self.poll_results()

    def lang_code(self) -> str:
        name = self.language.get()
        return next(code for code, label in self.langs.items() if label == name)

    def show(self, message: str, ok: bool = True) -> None:
        self.status.config(text=message, fg="green" if ok else "red")

    def speak(self) -> None:
        text, lang = self.entry.get("1.0", "end-1c"), self.lang_code()
        self.speak_button.config(state="disabled")
        self.show("Converting…")
        # The network call runs on a worker thread; on the UI thread it froze the window.
        threading.Thread(target=self._speak_worker, args=(text, lang), daemon=True).start()

    def _speak_worker(self, text: str, lang: str) -> None:
        try:
            synthesize(text, lang, self.audio)
            self.results.put(("converted", None))
            play(self.audio)
        except SpeechError as e:
            self.results.put(("failed", str(e)))

    def poll_results(self) -> None:
        """Applies worker results on the UI thread, then checks again shortly."""
        try:
            while True:
                kind, detail = self.results.get_nowait()
                if kind == "converted":
                    self._converted()
                else:
                    self._failed(detail)
        except queue.Empty:
            pass
        self.root.after(100, self.poll_results)

    def _converted(self) -> None:
        self.has_audio = True
        self.save_button.config(state="normal")
        self.speak_button.config(state="normal")
        self.show("Playing…")

    def _failed(self, message: str) -> None:
        self.speak_button.config(state="normal")
        self.show(message, ok=False)

    def save(self) -> None:
        target = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3", "*.mp3")])
        if target:
            shutil.copyfile(self.audio, target)
            self.show(f"Saved to {target}")

    def clear(self) -> None:
        self.entry.delete("1.0", "end")
        self.show("")


def main() -> None:
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
