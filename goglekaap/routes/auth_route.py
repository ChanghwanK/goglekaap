from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    session,
    request
)

from goglekaap.forms.auth_form import (
    LoginForm,
    RegisterForm
)

from goglekaap import db
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
        user = User.find_one_by_user_id(form.user_id.data)
        if user:
            if not security.check_password_hash(
                    user.password,
                    form.password.data
            ):
                flash('Password is not valid.')
            else:
                session['user_id'] = user.user_id
                return redirect(url_for('base.index'))
        else:
            flash('User ID is not exists.')
        return redirect(request.path)

    if session.get("user_id"):
        return redirect(url_for('base.index'))
    return render_template(f'{NAME}/login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    user_id = form.user_id.data

    if form.validate_on_submit():
        user = User.find_one_by_user_id(user_id)

        if user:
            flash('User ID is already exsits.')
            return redirect(request.path)
        else:
            user = User(
                user_id=user_id,
                user_name=form.user_name.data,
                password=security.generate_password_hash(form.password.data)
            )
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.user_id
        return redirect(url_for('base.index'))
    else:
        flash_form_errors(form)

    if session.get('user_id'):
        return redirect(url_for('base.index'))

    return render_template(f'{NAME}/register.html', form=form)


@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for(f'{NAME}.login'))


def flash_form_errors(form):
    for _, errors in form.errors.items():
        for error in errors:
            flash(error)
