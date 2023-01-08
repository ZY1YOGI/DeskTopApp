from ..lib import *
from ..Msg import Msg

class Validate:

    class Input:
        @staticmethod
        def INT(name: QLineEdit) -> QLineEdit.setValidator:
            return name.setValidator(QRegExpValidator(QRegExp('[0-9]{12}')))

        @staticmethod
        def FLOAT(name: QLineEdit) -> QLineEdit.setValidator:
            return name.setValidator(QRegExpValidator(QRegExp('[+-]?[0-9]+\\.[0-9]{2}')))

        @staticmethod
        def custom(name: QLineEdit, custom: QRegExp) -> QLineEdit.setValidator:
            return name.setValidator(QRegExpValidator(QRegExp(custom)))

        @staticmethod
        def EMAIL(email: str) -> bool:
            if email != "":
                if match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,5}$", email):
                    return True
                return False
            return True

    class Fields:
        @staticmethod
        def __init__(fields) -> None:
            if not fields:
                return False
                
            for field in fields:
                if fields[field]:
                    print(field, "->" , fields[field])

                if not fields[field]:
                    Msg(f"please Enter {field}")
                    break

            return False