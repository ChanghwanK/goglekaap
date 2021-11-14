from flask import Blueprint, render_template

# NAME은 namespace로 활용한다.
NAME = 'base'

bp = Blueprint(NAME, __name__)

@bp.route('/')
def index():
    return render_template('index.html')
