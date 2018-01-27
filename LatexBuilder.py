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

    def write_to_file(self, output_file=Config.LATEX_TARGET_FILE):
        expected_pages = len(Config.RAW_DATA) // Config.CARDS_PER_PAGE
        os.makedirs(Config.DIR_OUTPUT, exist_ok=True)
        print("Writing {} double-sided pages of output.".format(
                expected_pages
        ))

        # TODO: implement the actual page generation
        print("Omitting the not-implemented-yet page generation.")

        print("Done.")

