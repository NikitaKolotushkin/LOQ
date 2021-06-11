from flask import Flask, redirect
from flask_security import SQLAlchemyUserDatastore, url_for_security

from config import Config
from .extensions import migrate, login_manager, security


def create_app(config_class=Config):
    """
    Application factory method used to create and configure the application
    """

    app = Flask(__name__)
    app.config.from_object(config_class)

    init_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    """
    Register all application blueprints
    """
    from app.blueprints.main_page import main_page_bp
    from app.blueprints.auth import auth_bp

    app.register_blueprint(main_page_bp)
    app.register_blueprint(auth_bp)


def init_extensions(app: Flask):
    """
    Initialize all registered extensions (e.g. SQLAlchemy, BCrypt etc.)
    """

    # follow Flask recommendations to avoid circular dependencies
    # see https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/ and
    # https://stackoverflow.com/questions/22929839/circular-import-of-db-reference-using-flask-sqlalchemy-and-blueprints
    from .extensions import db
    from .models import User, Role

    db.init_app(app)
    migrate.init_app(app, db)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)

    security.init_app(app, datastore=user_datastore)

    login_manager.init_app(app)
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.login_manager.unauthorized_handler
    def unauth_handler():
        return redirect(url_for_security('login'))

    #
    # user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    # security.init_app(app, datastore=user_datastore, register_form=AfoRegistrationForm,
    #                   confirm_register_form=AfoRegistrationForm, login_form=AfoLoginForm,
    #                   forgot_password_form=PasswordResetForm, reset_password_form=PasswordResetSecondStep,
    #                   change_password_form=PasswordChangeForm)
