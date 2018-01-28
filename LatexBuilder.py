#!/usr/bin/env python3

from Config import Config
import math
import os

class LatexBuilder:
    """ Builds a LaTeX code which, when compiled, generates a PDF file
        with flashcards containing the loaded data.
    """

    PREAMBLE_FIXED = """\
\\documentclass[a4paper, landscape]{article}
\\usepackage{array}
\\usepackage[margin=0mm]{geometry}
\\usepackage[utf8]{inputenc}

\\newcolumntype{P}[1]{>{\\centering\\arraybackslash}p{#1}}
\\newcolumntype{M}[1]{@{}>{\\centering\\arraybackslash}m{#1}@{}}
\\setlength\\tabcolsep{0pt}
\\renewcommand\\arraystretch{0}
"""

    DOCUMENT_HEADER = """\
\\begin{document}
"""

    DOCUMENT_FOOTER = """\
\\end{document}
"""

    def __init__(self):
        self.preamble_userdefined = ""
        self.face_header = ""
        self.face_footer = ""
        self.reverse_header = ""
        self.reverse_footer = ""

    def recalculate_headers_and_footers(self):
        one_cell_tabular = "| M{{{:d}mm}} ".format(Config.CARD_WIDTH_MM)
        cells_tabular = one_cell_tabular * Config.CARD_COLUMNS_PER_PAGE
        inner_tabular = cells_tabular + "| @{}m{0pt}@{}"
        self.face_header="""\
  \\begin{table}
    \\centering
    \\begin{tabular}{ """ + inner_tabular + """ }
"""
        self.face_footer = """
    \\end{tabular}
  \\end{table}
"""

        one_cell_rev_tabular = "M{{1mm}} M{{{:d}mm}} M{{1mm}} ".format(
                Config.CARD_WIDTH_MM - 2)
        cells_rev_tabular = one_cell_rev_tabular * Config.CARD_COLUMNS_PER_PAGE
        inner_rev_tabular = cells_rev_tabular + "@{}m{0pt}@{}"
        self.reverse_header = """\
  \\begin{table}
    \\centering
    \\begin{tabular}{ """ + inner_rev_tabular + """ }
"""
        self.reverse_footer = """
    \\end{tabular}
  \\end{table}
"""
        print(self.face_header)
        print(self.face_footer)
        print(self.reverse_header)
        print(self.reverse_footer)

    def write_to_file(self, output_file=Config.LATEX_TARGET_FILE):
        self.recalculate_headers_and_footers()
        expected_pages = len(Config.RAW_DATA) // Config.CARDS_PER_PAGE

        os.makedirs(Config.DIR_OUTPUT, exist_ok=True)
        print("Writing {} double-sided pages of output.".format(
                expected_pages
        ))

        with open(Config.LATEX_TARGET_FILE, "w") as outfile:
            outfile.write(self.PREAMBLE_FIXED)
            outfile.write(self.DOCUMENT_HEADER)

            for page in range(expected_pages):
                face_page_contents = []
                reverse_page_contents = []
                for r in range(Config.CARD_ROWS_PER_PAGE):
                    face_line = ""
                    reverse_line = ""
                    for p in range(Config.CARD_COLUMNS_PER_PAGE):
                        face_line += "{:s} & ".format("x")
                        reverse_line += "{:s} & ".format("y")
                    face_line += "\\\\[{:d}mm]".format(Config.CARD_HEIGHT_MM)
                    face_page_contents.append(face_line)
                    face_page_contents.append("\\hline")

                    reverse_line += "\\\\[{:d}mm]".format(
                            Config.CARD_HEIGHT_MM)
                    reverse_page_contents.append(reverse_line)

                outfile.write(self.face_header)
                for line in face_page_contents:
                    outfile.write(line + "\n")
                outfile.write(self.face_footer)

                outfile.write(self.reverse_header)
                for line in reverse_page_contents:
                    outfile.write(line + "\n")
                outfile.write(self.reverse_footer)
                print("Completed setting page #{:d}/{:d}.".format(
                        page+1, expected_pages
                ))

            outfile.write(self.DOCUMENT_FOOTER)

        os.system("pdflatex --output-directory \"{}\" \"{}\"".format(
                Config.DIR_OUTPUT,
                Config.LATEX_TARGET_FILE
        ))

        print("Done.")

