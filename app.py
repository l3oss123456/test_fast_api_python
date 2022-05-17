from flask import Flask
from controller.employee import employee_blueprint
from controller.login import login_blueprint


app = Flask(__name__)
app.register_blueprint(employee_blueprint)
app.register_blueprint(login_blueprint)


if __name__ == "__main__":
    app.debug = True
    app.run()
