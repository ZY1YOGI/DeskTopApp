from Model.DB import DB
from lib.Validate import Validate


class UserModel:

    def Validate(self):
        pass

    @staticmethod
    def getAllUsers() -> list:
        return DB.QueryDB("SELECT name, phone, email FROM users WHERE act=1")

    @staticmethod
    def getUserById(id: int) -> list:
        return DB.QueryDB(f"SELECT  name, phone, email FROM users WHERE id={id} ")

    @staticmethod
    def storyUser(user: dict) -> DB.QueryDB:
        Validate.Fields(user)

        return DB.QueryDB(f"""INSERT INTO users (name, phone, email, password)
                            VALUES ('{user['name']}','{user['phone']}','{user['email']}', '{user['password']}')""")

    @staticmethod
    def updateUser(user: dict, id: int) -> DB.QueryDB:
        return DB.QueryDB(f"UPDATE users SET name='{user['name']}', phone='{user['phone']}', email='{user['email']}', password='{user['password']}' WHERE id={id} ")

    @staticmethod
    def getIdByName(name: str) -> int:
        return DB.QueryDB(f"SELECT id FROM users WHERE name='{name}'")

    @staticmethod
    def getNameById(id: int) -> str:
        return DB.QueryDB(f"SELECT name FROM users WHERE id={id} ")

    # login user with databases

    @staticmethod
    def LogIn(user: dict) -> DB.QueryDB:
        return DB.QueryDB(f"SELECT * FROM user WHERE name = '{user['username']}' AND password = '{user['password']}' ")
