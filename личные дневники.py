import json

from flask import Flask, request, render_template, session
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from tablet_of_users import UsersModel
from tablet_of_news import NewsModel
from DB import DB

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class AddNewsForm(FlaskForm):
    title = StringField('Заголовок новости', validators=[DataRequired()])
    content = TextAreaField('Текст новости', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


base = DB()
users_base = UsersModel(base)
with open("json_files/logins_passwords", "rt", encoding="utf8") as f:
    f = json.loads(f.read())
users_base.init_table()
for i in range(len(f)):
    users_base.insert(f[i]['login'], f[i]['password'])


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        exists = users_base.exists(request.form['username'], request.form['password'])
        if exists[0]:
            session['username'] = request.form['username']
            session['user_id'] = exists[1]
            return redirect('/success')
        return redirect('/failure')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success', methods=['GET', 'POST'])
def success():
    if 'username' not in session:
        return redirect('/login')
    news = NewsModel(base)
    news.init_table()
    news1 = news.get_all(session['user_id'])
    return render_template('index.html', username=session['username'],
                           news=news1)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
