import sys
import pyqtgraph as pg
from PyQt5 import QtWidgets

from View.MainView import MainView

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


if __name__ == '__main__':
    "Start"
    app = QtWidgets.QApplication(sys.argv)

    "Declare View"
    MainView = MainView()


    "Exit"
    sys.exit(app.exec())
