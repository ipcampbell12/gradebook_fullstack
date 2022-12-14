from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


if __name__ == 'main':
    db.init_app(app)
    app.run(debug=True)
