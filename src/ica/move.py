import tkinter as tk


class MoveWords:
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("Move Text")

        self.canvas = tk.Canvas(self.main, width=500, height=300, bg="lightblue")
        self.canvas.pack()

        self.text_id = self.canvas.create_text(
            250, 150,
            text="TongTong",
            fill="darkblue",
            font=("Arial", 20)
        )

        for key in ["w", "a", "s", "d",
                    "Up", "Down", "Left", "Right"]:
            self.main.bind(f"<{key}>", self.move_callback)

        self.main.mainloop()

    def move_callback(self, event):
        key = event.keysym

        if key in ("w", "Up"):
            self.canvas.move(self.text_id, 0, -10)
        elif key in ("s", "Down"):
            self.canvas.move(self.text_id, 0, 10)
        elif key in ("a", "Left"):
            self.canvas.move(self.text_id, -10, 0)
        elif key in ("d", "Right"):
            self.canvas.move(self.text_id, 10, 0)

MoveWords()