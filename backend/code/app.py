from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Ian"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boardgames.db'
#engine = create_engine('sqlite:///boardgames.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


if __name__ == 'main':
    db.init_app(app)
    app.run(debug=True)
