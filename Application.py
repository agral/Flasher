import tkinter as tk
from tkinter import filedialog

from Config import Config


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.sourcedata_path = None
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.lf_sourcedata = tk.LabelFrame(self, text="Source data:",
                padx=5, pady=5)
        self.lf_sourcedata.pack(padx=5, pady=5)

        self.lbl_sourcedata = tk.Label(
                self.lf_sourcedata, text="(none)")
        self.lbl_sourcedata.pack(side="left")
        self.btn_setsourcedata = tk.Button(
                self.lf_sourcedata, text="Change",
                command=self.invoke_sourcedata_dialog)
        self.btn_setsourcedata.pack(side="right")

        self.btn_quit = tk.Button(
                self, text="EXIT", command=self.master.destroy)
        self.btn_quit.pack(side="bottom")


    def invoke_sourcedata_dialog(self):
        self.sourcedata_path = tk.filedialog.askopenfilename(
                initialdir = Config.DIR_HOME,
                title = "Select source data file",
                filetypes = (("CSV files", "*.csv"), ("All files", "*.*"))
        )
        self.lbl_sourcedata["text"] = self.sourcedata_path or "(none)"

