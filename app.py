from flask import Flask
from main.api import api_bp


app = Flask(__name__)




if __name__ == '__main__':
    app.register_blueprint(api_bp)
    app.run(debug=True)