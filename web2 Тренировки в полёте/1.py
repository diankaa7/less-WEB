from flask import Flask, render_template, request, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    title = request.args.get('title', 'Заготовка')
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    prof_lower = prof.lower()
    if 'инженер' in prof_lower or 'строитель' in prof_lower:
        header = 'Инженерные тренажеры'
        image = url_for('static', filename='ing.png')
    else:
        header = 'Научные симуляторы'
        image = url_for('static', filename='sci.png')
    return render_template('training.html', title=header, header=header, image_url=image)


if __name__ == '__main__':
    app.run(port=8080, debug=True)