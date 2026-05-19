from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class DoubleLoginForm(FlaskForm):
    astronaut_id = StringField('ID астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('ID капитана', validators=[DataRequired()])
    captain_token = PasswordField('Токен капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/double_login', methods=['GET', 'POST'])
def double_login():
    form = DoubleLoginForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('double_login.html', title='Двойная аутентификация', form=form)


@app.route('/success')
def success():
    return render_template('base.html', title='Успешный доступ')


if __name__ == '__main__':
    app.run(port=8080, debug=True)