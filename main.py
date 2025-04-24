from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import importlib ,os ,pkgutil,inspect
from entity import *

package_dir = os.path.dirname(__file__)+ '/entity'
for _, module_name, _ in pkgutil.iter_modules([package_dir]):
    module = importlib.import_module(f'entity.{module_name}')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///huixue.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)