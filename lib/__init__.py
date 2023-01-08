from .lib import *


class SRC:
    def __init__(self) -> None:
        super(SRC, self).__init__()

    def InitSRC(self) -> None:
        self.CLICK(self.btn_Exit,       self.close)
        self.CLICK(self.btn_Minimized,  self.showMinimized)
        self.CLICK(self.btn_Minimized,  self.showMinimized)

        self.Hed_Main.mouseMoveEvent = self.MoveWindwo
        self.MainContent.tabBar().setVisible(False)

    def TABLEWIDGET(self, NameTable: QTableWidget, DATA: list) -> None:
        NameTable.setRowCount(0)
        NameTable.insertRow(0)
        for row, form in enumerate(DATA):
            for column, item in enumerate(form):
                NameTable.setItem(row, column, QTableWidgetItem(str(item)))
            row_position = NameTable.rowCount()
            NameTable.insertRow(row_position)
        NameTable.removeRow(NameTable.rowCount() - 1)

    def CLICK(self, btn, func) -> QPushButton.clicked:
        btn.clicked.connect(lambda: func())

    def MoveWindwo(self, event):
        try:
            if self.isMaximized() == False:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        except:
            None

    def mousePressEvent(self, event):
        try:
            self.clickPosition = event.globalPos()
        except:
            None

    def setTAB(self, id: int) -> None:
        self.MainContent.setCurrentIndex(id)
