from flask import Flask, render_template, session, request, make_response, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bc916900ed8190ab5ffa1943c63827ae3317d303'

#################################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'second'
login_manager.login_message = 'Для доступа к этой странице необходимо пройти аутентификацию.'
login_manager.login_message_category = 'info'

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

users = {'user' : User(1, 'user', 'qwerty'),}

@login_manager.user_loader
def load_user(user_id):
    for user in users.values():
        if user.id == int(user_id):
            return user
    return None


##################################

@app.route('/')
def index():
    return render_template('index.html', title = 'Лабораторная работа №3')


@app.route('/first')
def first():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return render_template('first.html', title='Счётчик посещений', visits = session['visits'])


@app.route('/second', methods = ['GET', 'POST'])
def second():
    error = None
    if current_user.is_authenticated:
        return '<h2>Вы уже авторизованы!</h2>'
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if request.form.get('remember'):
            remember = True
        else:
            remember = False

        user = users.get(username)
        if user and user.password == password:
            login_user(user, remember = remember)
            flash('Вы успешно вошли в систему!', 'success')
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            return redirect(url_for('index'))
        else:
            error = 'Неверное имя пользователя или пароль'
    return render_template('second.html', title='Аутентификация пользователей', error = error)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы', 'info')
    return redirect(url_for('index'))

@app.route('/third')
@login_required
def third():
    return render_template('third.html', title='Секретная страница')


if __name__ == '__main__':
    app.run(debug=True)
