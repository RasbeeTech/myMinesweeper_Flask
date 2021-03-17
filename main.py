from flask import Flask, render_template, request
from source import Minesweeper

app = Flask(__name__)


game = Minesweeper('medium')


@app.route('/')
def index():
    game.change_difficulty('medium')
    rows = columns = game.play_field()
    return render_template('index.html',
                           rows=rows, columns=columns,
                           difficulty='medium',
                           num_of_flags=game.mines,
                           mine_locations=game.mine_locations)


@app.route('/', methods=['POST', 'GET'])
def form_post():
    # TODO: render template partially
    if request.method == 'POST':
        keys = []
        for key in request.form.keys():
            keys.append(key)
        if 'difficulty' in keys:
            game.change_difficulty(request.form['difficulty'])
            rows = columns = game.play_field()
            return render_template('index.html',
                                   rows=rows,
                                   columns=columns,
                                   difficulty=game.difficulty,
                                   num_of_flags=game.mines,
                                   mine_locations=game.mine_locations)
        if 'tile' in keys:
            print(request.form['tile'])

            return '', 204  # HTTP empty response
