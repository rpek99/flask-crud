from flask import Flask, render_template
from .views import views
from .auth import auth
from .dbmodels import User, db
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sadsadsad13ewdwdfwef'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:localhost/db'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        user = User.query.get(int(id))
        return user

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html')

    return app
    
def create_database(app):
    db.create_all(app=app)

   