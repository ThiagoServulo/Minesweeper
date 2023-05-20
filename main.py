import sys
from Minesweeper import Minesweeper
from PySide2.QtWidgets import *


class CriarTelaPrincipal(QMainWindow, Minesweeper ):
    def __init__(self):
        """
        Constructor
        """
        super(CriarTelaPrincipal, self).__init__()
        self.setupUi(self)


# Entry point of the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CriarTelaPrincipal()
    window.show()
    sys.exit(app.exec_())
