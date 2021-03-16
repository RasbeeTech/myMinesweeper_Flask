from flask import Flask, render_template, request

app = Flask(__name__)


def play_field(difficulty):
    if difficulty == 'easy':
        return list(range(0, 11))
    if difficulty == 'medium':
        return list(range(0, 16))
    if difficulty == 'hard':
        return list(range(0, 21))


@app.route('/')
def index():
    rows = play_field('easy')
    columns = play_field('easy')
    return render_template('index.html', rows=rows, columns=columns, difficulty='medium')


@app.route('/', methods=['POST', 'GET'])
def form_post():
    if request.method == 'POST':
        # TODO: render template partially
        rows = play_field(request.form['difficulty'])
        columns = play_field(request.form['difficulty'])
        return render_template('index.html', rows=rows, columns=columns, difficulty=request.form['difficulty'])
