from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

PROFESSIONS = [
    'Инженер-исследователь',
    'Пилот',
    'Строитель',
    'Экзобиолог',
    'Врач',
    'Инженер по терраформированию',
    'Климатолог',
    'Специалист по радиационной защите',
    'Астрогеолог',
    'Гляциолог',
    'Инженер жизнеобеспечения',
    'Метеоролог',
    'Оператор марсохода',
    'Космобиолог',
    'Штурман'
]


@app.route('/')
@app.route('/index')
def index():
    title = request.args.get('title', 'Заготовка')
    return render_template('base.html', title=title)


@app.route('/list_prof/<list_param>')
def list_prof(list_param):
    return render_template('list_prof.html',
                           title='Список профессий',
                           list_type=list_param,
                           professions=PROFESSIONS)


if __name__ == '__main__':
    app.run(port=8080, debug=True)