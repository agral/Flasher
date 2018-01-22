#!/usr/bin/env python3

import tkinter as tk
from Application import Application


def main():
    tk_root = tk.Tk()
    app = Application(master=tk_root)
    app.master.title = "Flasher"
    app.mainloop()


if __name__ == "__main__":
    main()
