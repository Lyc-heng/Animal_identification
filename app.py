from flask import render_template, redirect, url_for, request

from flask_login import LoginManager, login_required, login_user, logout_user

import os

from date_base import create_app
from date import User

app = create_app()
app.secret_key = 'LearnFlaskTheHardWay2017'


# Add LoginManager
login_manager = LoginManager()
login_manager.session_protection = 'AdminPassword4Me'
login_manager.login_view = 'signin'
login_manager.login_message = 'Unauthorized User'
login_manager.login_message_category = "info"
login_manager.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/date', methods=['GET', 'POST'])
def date():
    out = []
    for i in range(1, len(User.query.all()) + 1):
        out.append(User.query.filter_by(id=i).first().animals)
    print(out)
    print(type(out))
    return str(out)


if __name__ == "__main__":
    app.run(debug=True)

