from flask_login import LoginManager
from flask_security import Security
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
login_manager = LoginManager()
security = Security()
