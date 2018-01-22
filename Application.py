import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.btn_quit = tk.Button(
                self, text="EXIT", command=self.master.destroy)
        self.btn_quit.pack(side="bottom")


