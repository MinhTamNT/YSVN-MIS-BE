import pyodbc
from flask import Flask
import cloudinary
import cloudinary.uploader



app = Flask(__name__)
app.secret_key = '*(&*(@*&(*@(^!(*@75876528378932^@%*&^(*@*@&#*'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = '38a5f73c-ff0f-4b81-b466-701071019a4d'


from cloudinary.utils import cloudinary_url
connection_string = (
    r"Driver={ODBC Driver 17 for SQL Server};"
    r"Server=DESKTOP-CKADOQQ\SQLEXPRESS;"  
    "Database=YSVNMIS;"  
    "UID=sa;"  
    "PWD=123456;"
)

cloudinary.config(
    cloud_name = "dwvg5xlum",
    api_key = "922611133231776",
    api_secret = "Q0bJhJc_3Z06xk1mFMf0oDSgWxo", # Click 'View API Keys' above to copy your API secret
    secure=True
)

try:
    connection = pyodbc.connect(connection_string)
    print("Kết nối thành công!")
except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    print(ex)
    print(f"Error: {sqlstate}")


def get_connection():
    try:
        connection = pyodbc.connect(connection_string)
        return connection
    except pyodbc.Error as ex:
        print(f"Error: {ex}")
        return None

