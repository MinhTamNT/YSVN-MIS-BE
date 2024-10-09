import pyodbc
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)

app.secret_key = '*(&*(@*&(*@(^!(*@75876528378932^@%*&^(*@*@&#*'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = '38a5f73c-ff0f-4b81-b466-701071019a4d'


connection_string = (
    r"Driver={ODBC Driver 17 for SQL Server};"
    r"Server=DESKTOP-CKADOQQ\SQLEXPRESS;"  
    "Database=YSVNMIS;"  
    "UID=sa;"  
    "PWD=123456;"
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

swagger_template = {
    "info": {
        "title": "MSI API",
        "description": "API document",
        "version": "1.0.0"
    },
    "host": "localhost:5000",
    "basePath": "/",
    "schemes": ["http", "https"]
}
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # Include all routes
            "model_filter": lambda tag: True,  # Include all models
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}
Swagger(app, template=swagger_template, config=swagger_config)