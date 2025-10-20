from flask import Flask

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='what to do'

    from .views import views # type: ignore
    from .auth import auth # type: ignore

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/auth')

    return app