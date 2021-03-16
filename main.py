from flask import Flask, render_template, request
from source import Minesweeper

app = Flask(__name__)

game = Minesweeper('medium')


def play_field(difficulty):
    if difficulty == 'easy':
        return list(range(0, 6))
    if difficulty == 'medium':
        return list(range(0, 9))
    if difficulty == 'hard':
        return list(range(0, 12))


@app.route('/')
def index():
    game.change_difficulty('medium')
    rows = columns = play_field('medium')
    return render_template('index.html', rows=rows, columns=columns, difficulty='medium', num_of_flags=game.mines)


@app.route('/', methods=['POST', 'GET'])
def form_post():
    # TODO: Set number of flags remaining
    # TODO: render template partially
    if request.method == 'POST':
        keys = []
        for key in request.form.keys():
            keys.append(key)
        if 'difficulty' in keys:
            game.change_difficulty(request.form['difficulty'])
            rows = columns = play_field(request.form['difficulty'])
            return render_template('index.html', rows=rows, columns=columns, difficulty=request.form['difficulty'])
        if 'tile' in keys:
            print(request.form['tile'])
            return '', 204  # HTTP empty response
