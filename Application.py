import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from Config import Config
from Utils import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.outfile_path = Config.DIR_OUTPUT_DEFAULT

        master.minsize(
                width=Config.MAIN_WINDOW_WIDTH,
                height=Config.MAIN_WINDOW_HEIGHT)
        self.pack(fill="both", expand="yes")
        self.create_widgets()
        self.recalculate_and_update_geometry()

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
        self.lf_pagegeometry.grid(row=0, column=0, sticky="nw")

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
        self.lbl_pagegeometry_width.grid(row=0, column=0, sticky="w")
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
        self.lbl_pagegeometry_height.grid(row=1, column=0, sticky="w")
        self.edt_pagegeometry_height.grid(row=1, column=1)
        self.lbl_pagegeometry_height_mm.grid(row=1, column=2)

        # Adds the "Card geometry" group to the "Geometry (...) setup" group:
        self.lf_cardgeometry = tk.LabelFrame(
                self.lf_layoutsetup, text="Card geometry",
                padx=3, pady=3
        )
        self.lf_cardgeometry.grid(row=0, column=1, sticky="nw", padx=8)

        self.lbl_cardgeometry_width = tk.Label(
                self.lf_cardgeometry, text="Width:")
        self.edt_cardgeometry_width_text = tk.StringVar()
        self.edt_cardgeometry_width = tk.Entry(
                self.lf_cardgeometry,
                textvariable=self.edt_cardgeometry_width_text,
                width=5)
        self.edt_cardgeometry_width_text.set(Config.DEFAULT_CARD_WIDTH_MM)
        self.lbl_cardgeometry_width_mm = tk.Label(
                self.lf_cardgeometry, text="mm")
        self.lbl_cardgeometry_width.grid(row=0, column=0, sticky="w")
        self.edt_cardgeometry_width.grid(row=0, column=1)
        self.lbl_cardgeometry_width_mm.grid(row=0, column=2)

        self.lbl_cardgeometry_height = tk.Label(
                self.lf_cardgeometry, text="Height:")
        self.edt_cardgeometry_height_text = tk.StringVar()
        self.edt_cardgeometry_height = tk.Entry(
                self.lf_cardgeometry,
                textvariable=self.edt_cardgeometry_height_text,
                width=5)
        self.edt_cardgeometry_height_text.set(Config.DEFAULT_CARD_HEIGHT_MM)
        self.lbl_cardgeometry_height_mm = tk.Label(
                self.lf_cardgeometry, text="mm")
        self.lbl_cardgeometry_height.grid(row=1, column=0, sticky="w")
        self.edt_cardgeometry_height.grid(row=1, column=1)
        self.lbl_cardgeometry_height_mm.grid(row=1, column=2)

        # Adds the button to recalculate the geometry:
        self.btn_recalculate = tk.Button(
                self.lf_layoutsetup, text="Recalculate",
                command=self.recalculate_and_update_geometry
        )
        self.btn_recalculate.grid(row=0, column=2, sticky="nesw")

        # Adds the "Summary" group to the "Geometry (...) setup" group:
        self.lf_summary = tk.LabelFrame(
                self.lf_layoutsetup, text="Summary",
                padx=3, pady=3
        )
        self.lf_summary.grid(row=0, column=3, sticky="nw", padx=8)
        self.lbl_summary_page_fixed = tk.Label(
                self.lf_summary, text="Page geometry:")
        self.lbl_summary_page_dim = tk.Label(
                self.lf_summary, text="-")
        self.lbl_summary_page_mm = tk.Label(
                self.lf_summary, text="mm")
        self.lbl_summary_page_fixed.grid(row=0, column=0, sticky="e")
        self.lbl_summary_page_dim.grid(row=0, column=1, sticky="e")
        self.lbl_summary_page_mm.grid(row=0, column=2, sticky="w")

        self.lbl_summary_card_fixed = tk.Label(
                self.lf_summary, text="Card geometry:")
        self.lbl_summary_card_dim = tk.Label(
                self.lf_summary, text="-")
        self.lbl_summary_card_mm = tk.Label(
                self.lf_summary, text="mm")
        self.lbl_summary_card_fixed.grid(row=1, column=0, sticky="e")
        self.lbl_summary_card_dim.grid(row=1, column=1, sticky="e")
        self.lbl_summary_card_mm.grid(row=1, column=2, sticky="w")

        # Adds a 30px of margin between the columns:
        self.lf_summary.grid_columnconfigure(3, minsize=30)

        self.lbl_cardsperpage_fixed = tk.Label(
                self.lf_summary, text="Cards per page:")
        self.lbl_cardsperpage = tk.Label(self.lf_summary, text="-")
        self.lbl_gridlayout_fixed_pre = tk.Label(
                self.lf_summary, text="(arranged in a ")
        self.lbl_gridlayout = tk.Label(self.lf_summary, text="-")
        self.lbl_gridlayout_fixed_post = tk.Label(
                self.lf_summary, text=" grid)")
        self.lbl_cardsperpage_fixed.grid(
                row=0, column=4, columnspan=2, sticky="e")
        self.lbl_cardsperpage.grid(row=0, column=6, sticky="w")
        self.lbl_gridlayout_fixed_pre.grid(row=1, column=4, sticky="e")
        self.lbl_gridlayout.grid(row=1, column=5, sticky="e")
        self.lbl_gridlayout_fixed_post.grid(row=1, column=6, sticky="w")

        self.btn_golatex = tk.Button(
                self, text="Go",
                command=self.cb_build
        )
        self.btn_golatex.pack(padx=20, pady=20)

        self.btn_quit = tk.Button(
                self, text="EXIT",
                command=self.master.destroy
        )
        self.btn_quit.pack(side="bottom")

    def invoke_sourcedata_dialog(self):

        Config.PATH_SOURCEDATA = tk.filedialog.askopenfilename(
                initialdir=Config.DIR_INPUT_DEFAULT,
                title="Select source data file",
                filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )
        self.lbl_sourcedata["text"] = Config.PATH_SOURCEDATA or "(none)"

    def invoke_setoutputdir_dialog(self):
        self.outfile_path = tk.filedialog.askdirectory(
                initialdir=self.outfile_path,
                title="Select output directory")
        self.lbl_outputdir["text"] = self.outfile_path or "(none)"

    def invoke_import(self):
        if Config.PATH_SOURCEDATA is None:
            tk.messagebox.showinfo(
                    "Failure",
                    "Please select the input file first."
            )
        else:
            Config.RAW_DATA = import_CSV_data_from_file(
                    Config.PATH_SOURCEDATA,
                    separator="|",
                    comment_token="#")

            tk.messagebox.showinfo(
                    "Success",
                    "Successfully imported {} records.".format(
                            len(Config.RAW_DATA))
            )

    def recalculate_and_update_geometry(self):
        pw = self.edt_pagegeometry_width_text.get()
        ph = self.edt_pagegeometry_height_text.get()
        cw = self.edt_cardgeometry_width_text.get()
        ch = self.edt_cardgeometry_height_text.get()

        ipw = iph = icw = ich = 0

        # Performs sanity-checks - all the numbers should be positive integers:
        try:
            if not pw.isdigit() or not pw.isdigit():
                raise ValueError()
            ipw = int(pw)
            iph = int(ph)
        except ValueError:
            tk.messagebox.showerror(
                    "Value error",
                    "Incorrect value for page width or height"
            )
            return

        try:
            if not cw.isdigit() or not ch.isdigit():
                raise ValueError()
            icw = int(cw)
            ich = int(ch)
        except ValueError:
            tk.messagebox.showerror(
                    "Value error",
                    "Incorrect value for card width or height"
            )
            return

        if icw > ipw or ich > iph:
            tk.messagebox.showerror(
                    "Dimension error",
                    "Card dimensions exceed page dimensions"
            )
            return

        Config.PAGE_WIDTH_MM = ipw
        Config.PAGE_HEIGHT_MM = iph
        Config.CARD_WIDTH_MM = icw
        Config.CARD_HEIGHT_MM = ich

        self.lbl_summary_page_dim["text"] = "{}x{}".format(
                Config.PAGE_WIDTH_MM, Config.PAGE_HEIGHT_MM
        )
        self.lbl_summary_card_dim["text"] = "{}x{}".format(
                Config.CARD_WIDTH_MM, Config.CARD_HEIGHT_MM
        )

        Config.CARD_COLUMNS_PER_PAGE = \
            Config.PAGE_WIDTH_MM // Config.CARD_WIDTH_MM
        Config.CARD_ROWS_PER_PAGE = \
            Config.PAGE_HEIGHT_MM // Config.CARD_HEIGHT_MM
        Config.CARDS_PER_PAGE = \
            Config.CARD_COLUMNS_PER_PAGE * Config.CARD_ROWS_PER_PAGE

        self.lbl_cardsperpage["text"] = str(Config.CARDS_PER_PAGE)
        self.lbl_gridlayout["text"] = "{}x{}".format(
                Config.CARD_COLUMNS_PER_PAGE, Config.CARD_ROWS_PER_PAGE
        )

    def cb_build(self):
        if len(Config.RAW_DATA) == 0:
            tk.messagebox.showerror(
                    "Failure",
                    "There is no data to process.\n" +
                    "Please import the data first."
            )
            return
        print("Build")
