from mysql.connector import connect
from lib.Msg import Msg
from re import compile


class DB:

    @classmethod
    def CONECT_DATABASE(self):
        try:
            self.db = connect(host="localhost", database="testing", user="root", password="012369510")
            self.cur = self.db.cursor()

            print("DB CONECT")
        except Exception as E:
            print(f"ERROR DATABASE: {E}")
            exit()

    @classmethod
    def QueryDB(self, query: str):
        try:
            self.cur.execute(query)
            if "UPDATE" in query or "INSERT" in query or "DELETE" in query:
                return self.db.commit()

            if query != "":
                result = self.cur.fetchall()
                self.db.commit()
                return result

            else:
                print("please Enter Query DB")
            self.db.commit()

        except AttributeError:
            print(f"DATABASE CONECT ERROR:")

        except Exception as E:
            ERROR = str(E)
            if "Duplicate" in ERROR:
                e = compile("\'(.*?)\'").findall(ERROR)[1]
                Msg(f"The {e} Is use")
            print(f"QueryDB: {ERROR}")
