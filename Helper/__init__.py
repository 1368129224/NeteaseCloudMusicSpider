import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def getMySqlTx():
    from config import MySqlStr
    return MySqlStr