from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon

from Model.TimeAxis.TimeAxisItem import TimeAxisItem


class MainView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi("dataview.ui")
        self.ui.show()

        self.ui.setWindowTitle("HEROS DATAVIEW")
        # self.ui.setWindowIcon(QIcon('icon.ico'))

        self.declare_graph()

    def declare_graph(self):
        self.pw1 = self.ui.graphWidget
        self.pw1.setAxisItems({'bottom': TimeAxisItem(orientation='bottom')})