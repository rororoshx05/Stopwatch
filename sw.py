import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.label = tk.Label(root, text="0:00", font=("Helvetica", 48))
        self.label.pack()

        self.start_button = tk.Button(root, text="Start", width=10, command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", width=10, command=self.stop)
        self.stop_button.pack()

        self.reset_button = tk.Button(root, text="Reset", width=10, command=self.reset)
        self.reset_button.pack()

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            minutes = int(self.elapsed_time // 60)
            seconds = int(self.elapsed_time % 60)
            self.label.config(text=f"{minutes}:{seconds:02d}")
            self.root.after(100, self.update_time)

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_time()
            self.start_button.config(text="Pause")

    def stop(self):
        if self.running:
            self.running = False
            self.start_button.config(text="Resume")

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.label.config(text="0:00")
        self.start_button.config(text="Start")

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
