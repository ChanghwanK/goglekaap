from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    session
)

from goglekaap.forms.auth_form import (
    LoginForm,
    RegisterForm
)

from goglekaap.model.user import User
from werkzeug import security

NAME = 'auth'
bp = Blueprint(NAME, __name__, url_prefix='/auth')


@bp.route('/')
def index():
    return redirect(url_for(f'{NAME}.login'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # POST, validate == OK
    if form.validate_on_submit():
        # TODO
        # 유저 조회
        # 유저 이미 존재하는지 체크
        # 없으면 유저 생성
        # 로그인 유저 (세션)
        user_id = form.data.get('user_id')
        password = form.data.get('password')
        return f'{user_id}, {password}'
    else:
        flash_form_errors(form)
        pass
    return render_template(f'{NAME}/login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # TODO
        # 유저조회
        # 없으면 생성
        # 생성된 유저를 로그인 유지 (세션)


        user_id = form.data.get('user_id')
        user_name = form.data.get('user_name')
        password = form.data.get('password')
        repassword = form.data.get('repassword')
        return f'{user_id},{user_name}, {password}, {repassword}'
    else:
        flash_form_errors(form)
        pass
    return render_template(f'{NAME}/register.html', form=form)


@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for(f'{NAME}.login'))


def flash_form_errors(form):
    for _, errors in form.errors.items():
        for error in errors:
            flash(error)