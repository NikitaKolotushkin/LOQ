from app import create_app
from config import DebugConfig


app = create_app(config_class=DebugConfig)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'],
            use_reloader=app.config['RELOADER'])
