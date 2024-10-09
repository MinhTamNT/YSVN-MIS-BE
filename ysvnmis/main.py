from flask import app
from ysvnmis import app
import ysvnmis.api.collaborate.collabortae_api

if __name__ == "__main__":
    with app.app_context():
        app.run(host='0.0.0.0', port=5000 , debug=True)