import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from Config import Config
from Utils import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.sourcedata_path = None
        self.outfile_path = Config.DIR_OUTPUT_DEFAULT
        self.raw_data = []

        master.minsize(
                width=Config.MAIN_WINDOW_WIDTH,
                height=Config.MAIN_WINDOW_HEIGHT)
        self.pack(fill="both", expand="yes")
        self.create_widgets()

    def create_widgets(self):
        # Adds the "Source data" group to the main window:
        self.lf_sourcedata = tk.LabelFrame(
                self, text="Source data:",
                padx=5, pady=5
        )
        self.lf_sourcedata.pack(padx=5, pady=5, fill="x")
        self.lbl_sourcedata = tk.Label(
                self.lf_sourcedata, text="(none)")
        self.lbl_sourcedata.grid(row=0, column=0, sticky="w")
        self.btn_setsourcedata = tk.Button(
                self.lf_sourcedata, text="Change",
                command=self.invoke_sourcedata_dialog)
        self.btn_setsourcedata.grid(row=0, column=1)
        self.btnimport = tk.Button(
                self.lf_sourcedata, text="Import",
                command=self.invoke_import
        )
        self.btnimport.grid(row=0, column=2)
        self.lf_sourcedata.columnconfigure(0, weight=1)

        # Adds the "Output" group to the main window:
        self.lf_outputdir = tk.LabelFrame(
                self, text="Output directory:",
                padx=5, pady=5
        )
        self.lf_outputdir.pack(padx=5, pady=5, fill="x")
        self.lbl_outputdir = tk.Label(
                self.lf_outputdir, text=self.outfile_path)
        self.lbl_outputdir.grid(row=0, column=0, sticky="w")
        self.btn_setoutputdir = tk.Button(
                self.lf_outputdir, text="Change",
                command=self.invoke_setoutputdir_dialog
        )
        self.btn_setoutputdir.grid(row=0, column=1)
        self.lf_outputdir.columnconfigure(0, weight=1)

        # Adds the "Geometry and layout setup" group to the main window:
        self.lf_layoutsetup = tk.LabelFrame(
                self, text="Geometry and layout setup",
                padx=5, pady=5
        )
        self.lf_layoutsetup.pack(padx=5, pady=5, fill="x")

        # Adds the "Page geometry" group to the "Geometry (...) setup" group:
        self.lf_pagegeometry = tk.LabelFrame(
                self.lf_layoutsetup, text="Page geometry",
                padx=3, pady=3
        )
        self.lf_pagegeometry.grid(row=0, column=0)

        self.lbl_pagegeometry_width = tk.Label(
                self.lf_pagegeometry, text="Width:")
        self.edt_pagegeometry_width_text = tk.StringVar()
        self.edt_pagegeometry_width = tk.Entry(
                self.lf_pagegeometry,
                textvariable=self.edt_pagegeometry_width_text,
                width=5)
        self.edt_pagegeometry_width_text.set(Config.DEFAULT_PAGE_WIDTH_MM)
        self.lbl_pagegeometry_width_mm = tk.Label(
                self.lf_pagegeometry, text="mm")
        self.lbl_pagegeometry_width.grid(row=0, column=0)
        self.edt_pagegeometry_width.grid(row=0, column=1)
        self.lbl_pagegeometry_width_mm.grid(row=0, column=2)

        self.lbl_pagegeometry_height = tk.Label(
                self.lf_pagegeometry, text="Height:")
        self.edt_pagegeometry_height_text = tk.StringVar()
        self.edt_pagegeometry_height = tk.Entry(
                self.lf_pagegeometry,
                textvariable=self.edt_pagegeometry_height_text,
                width=5)
        self.edt_pagegeometry_height_text.set(Config.DEFAULT_PAGE_HEIGHT_MM)
        self.lbl_pagegeometry_height_mm = tk.Label(
                self.lf_pagegeometry, text="mm")
        self.lbl_pagegeometry_height.grid(row=1, column=0)
        self.edt_pagegeometry_height.grid(row=1, column=1)
        self.lbl_pagegeometry_height_mm.grid(row=1, column=2)

        self.btn_quit = tk.Button(
                self, text="EXIT",
                command=self.master.destroy
        )
        self.btn_quit.pack(side="bottom")

    def invoke_sourcedata_dialog(self):
        self.sourcedata_path = tk.filedialog.askopenfilename(
                initialdir=Config.DIR_INPUT_DEFAULT,
                title="Select source data file",
                filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )
        self.lbl_sourcedata["text"] = self.sourcedata_path or "(none)"

    def invoke_setoutputdir_dialog(self):
        self.outfile_path = tk.filedialog.askdirectory(
                initialdir=self.outfile_path,
                title="Select output directory")
        self.lbl_outputdir["text"] = self.outfile_path or "(none)"

    def invoke_import(self):
        if self.sourcedata_path is None:
            tk.messagebox.showinfo(
                    "Failure",
                    "Please select the input file first."
            )
        else:
            self.raw_data = import_CSV_data_from_file(
                    self.sourcedata_path,
                    separator="|",
                    comment_token="#")

            tk.messagebox.showinfo(
                    "Success",
                    "Successfully imported {} records.".format(
                            len(self.raw_data))
            )
