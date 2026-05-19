from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    title = request.args.get('title', 'Заготовка')
    return render_template('base.html', title=title)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    params = {
        'title': request.args.get('title', 'Mars One'),
        'surname': request.args.get('surname', 'Watny'),
        'name': request.args.get('name', 'Mark'),
        'education': request.args.get('education', 'выше среднего'),
        'profession': request.args.get('profession', 'штурман марсохода'),
        'sex': request.args.get('sex', 'male'),
        'motivation': request.args.get('motivation',
                                       'Всегда мечтал застрять на Марсе!'),
        'ready': request.args.get('ready', 'True')
    }
    return render_template('auto_answer.html', **params)


if __name__ == '__main__':
    app.run(port=8080, debug=True)