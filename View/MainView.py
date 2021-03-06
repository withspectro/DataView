from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon


class MainView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi("dataview.ui")
        self.ui.show()

        self.ui.setWindowTitle("HEROS DATAVIEW")
        # self.ui.setWindowIcon(QIcon('icon.ico'))


    def declare_graph(self):
        self.pw1 = self.ui.graph_Widget_1
        self.pw1.setTitle("Conc data")
        self.pw1.setLabel(axis ='left', text= 'NH3(ppb)')
        self.pw1.setAxisItems({'bottom': TimeAxisItem(orientation='bottom')})