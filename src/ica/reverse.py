import tkinter as tk

class ReverseGUI:
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("Reverse String")

        tk.Label(self.main, text="Type something and press Enter:").pack()
        self.entry = tk.Entry(self.main, width=40)
        self.entry.pack()

        self.output_label = tk.Label(self.main, text="", font=("Arial", 14))
        self.output_label.pack()

        self.entry.bind("<Return>", self.entry_response)
        self.entry.bind("<Tab>", self.entry_response)

        tk.Button(self.main, text="Quit", command=self.main.destroy).pack(pady=5)

        self.main.mainloop()

    def entry_response(self, event):
        text = self.entry.get()
        reversed_text = text[::-1]
        self.output_label.config(text=reversed_text)


ReverseGUI()