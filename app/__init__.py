from flask import Flask
from flask_mail import Mail
from .routes import main

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    mail.init_app(app)
    app.register_blueprint(main)

    return app
