from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    from .controllers import register_controllers
    register_controllers(app)
    return app