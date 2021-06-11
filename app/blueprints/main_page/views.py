from flask import render_template
from flask_login import login_required

from app.blueprints.main_page.blueprint import main_page_bp


@main_page_bp.route('/')
def index():
    return render_template('main_page/index.html')


@main_page_bp.route('/second_page')
@login_required
def second_page():
    return render_template('main_page/second.html')
