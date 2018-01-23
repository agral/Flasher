import tkinter as tk
from tkinter import filedialog

from Config import Config


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.sourcedata_path = None
        self.outfile_path = Config.DIR_OUTPUT_DEFAULT

        master.minsize(
                width=Config.MAIN_WINDOW_WIDTH,
                height=Config.MAIN_WINDOW_HEIGHT)
        self.pack(fill="both", expand="yes")
        self.create_widgets()


    def create_widgets(self):
        self.lf_sourcedata = tk.LabelFrame(self, text="Source data:",
                padx=5, pady=5)
        self.lf_sourcedata.pack(padx=5, pady=5, fill="x")
        self.lbl_sourcedata = tk.Label(
                self.lf_sourcedata, text="(none)")
        self.lbl_sourcedata.grid(row=0, column=0, sticky="w")
        self.btn_setsourcedata = tk.Button(
                self.lf_sourcedata, text="Change",
                command=self.invoke_sourcedata_dialog)
        self.btn_setsourcedata.grid(row=0, column=1)
        self.lf_sourcedata.columnconfigure(0, weight=1)

        self.lf_outputdir = tk.LabelFrame(self, text="Output directory:",
                padx=5, pady=5)
        self.lf_outputdir.pack(padx=5, pady=5, fill="x")
        self.lbl_outputdir = tk.Label(
                self.lf_outputdir, text=self.outfile_path)
        self.lbl_outputdir.grid(row=0, column=0, sticky="w")
        self.btn_setoutputdir = tk.Button(
                self.lf_outputdir, text="Change",
                command=self.invoke_setoutputdir_dialog)
        self.btn_setoutputdir.grid(row=0, column=1)
        self.lf_outputdir.columnconfigure(0, weight=1)

        self.btn_quit = tk.Button(
                self, text="EXIT", command=self.master.destroy)
        self.btn_quit.pack(side="bottom")


    def invoke_sourcedata_dialog(self):
        self.sourcedata_path = tk.filedialog.askopenfilename(
                initialdir = Config.DIR_APP_ROOT,
                title = "Select source data file",
                filetypes = (("CSV files", "*.csv"), ("All files", "*.*"))
        )
        self.lbl_sourcedata["text"] = self.sourcedata_path or "(none)"


    def invoke_setoutputdir_dialog(self):
        self.outfile_path = tk.filedialog.askdirectory(
                initialdir = self.outfile_path,
                title = "Select output directory")
        self.lbl_outputdir["text"] = self.outfile_path or "(none)"
