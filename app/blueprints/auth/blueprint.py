from flask import Blueprint, request, abort, render_template, redirect, url_for
from flask_login import login_user, logout_user
from flask_security.utils import hash_password

from app.blueprints.auth.forms import SignupForm
from app.extensions import db
from app.models import User

auth_bp = Blueprint('auth', __name__)


# @auth_bp.route('/login')
# def login():
#     login_user(User.query.first())
#     return 'Login'


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        if User.query.filter(User.email == form.email.data).count():
            abort(400)
        user = User()
        user.password = hash_password(form.password.data)
        user.email = form.email.data
        db.session.add(user)
        db.session.commit()

        login_user(user)

        return redirect(url_for('main_page.index'))

    return render_template('main_page/signup.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_page.index'))
