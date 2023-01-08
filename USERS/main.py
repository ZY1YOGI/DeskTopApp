from lib import *
from lib.Msg import Msg
from lib.Validate import Validate
from Model.User import UserModel
UserUi, _ = loadUiType("UI/userUi.ui")
LogInUi, _ = loadUiType("UI/logInUi.ui")


class LogIn(QMainWindow, LogInUi, SRC):
    def __init__(self):
        super(LogIn, self).__init__()
        QMainWindow.__init__(self)
        SRC.__init__(self)
        self.setupUi(self)

    def CLICKED(self) -> None:
        pass


class Users(QMainWindow, UserUi, SRC):
    def __init__(self):
        super(Users, self).__init__()
        QMainWindow.__init__(self)
        SRC.__init__(self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.storyUser()
        # self.showUsers()

    def showUsers(self):
        print(UserModel.getAllUsers())
        self.TABLEWIDGET(self.tableWidget, UserModel.getAllUsers())
        self.CLICK(self.pushButton, lambda: self.storyUser())

    def storyUser(self) -> UserModel.storyUser:

        UserFields = {
            "name": "Ahmed",
            "phone": "010000",
            "email": "Ahmed@Gmail.com",
            "password": "15935782@#s"
        }

        UserModel.storyUser(UserFields)
        self.TABLEWIDGET(self.tableWidget, UserModel.getAllUsers())
