from lib.lib import *


Msg_Window, _ = loadUiType("UI/msgUi.ui")


class Msg(QMainWindow, Msg_Window):
    def __init__(self, msg: str = "", sleep: int = 1.5, mood: str = "Error"):
        super().__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.TEXT.setText(
            f"<html><head/><body><p align='center'>{msg}</p></body></html>")
        if mood == "Done":
            self.label.setPixmap(QPixmap(":img/icons/Done-icon.png"))
        elif mood == "Logo":
            self.label.setPixmap(QPixmap(":img/icons/Logo-icon.png"))

        elif mood == "Error":
            self.label.setPixmap(QPixmap(":img/icons/Error-icon.png"))

        self.sleep = sleep
        self.show()
        Thread(target=self.Exit).start()

    def Exit(self) -> QMainWindow.close:
        sleep(self.sleep)
        self.close()
