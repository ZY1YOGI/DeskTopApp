from lib import *
from USERS.main import Users, LogIn
from Model.DB import DB

MainUi, _ = loadUiType("UI/mainUi.ui")


class Main(QMainWindow, MainUi, SRC):
    def __init__(self):
        super(Main, self).__init__()
        QMainWindow.__init__(self)
        SRC.__init__(self)
        self.setupUi(self)
        self.InitSRC()
        self.CLICKED()

    def CLICKED(self) -> None:
        self.CLICK(self.btn_Home, lambda: self.setTAB(0))
        self.CLICK(self.btn_Users, lambda: self.setTAB(2))

    def test(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    DB.CONECT_DATABASE()
    window = Users()
    window.show()
    sys.exit(app.exec())
