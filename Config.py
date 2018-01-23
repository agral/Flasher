import os


class Config:
    MAIN_WINDOW_WIDTH = 800
    MAIN_WINDOW_HEIGHT = 600
    DIR_HOME = os.path.expanduser("~")
    DIR_APP_ROOT = os.path.dirname(os.path.realpath(__file__))

    DEFAULT_PDF_FILENAME = "output.pdf"
    DIR_OUTPUT_DEFAULT = os.path.join(DIR_APP_ROOT, "out")
    def __init__(self):
        pass
