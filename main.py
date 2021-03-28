from flask import Flask, render_template, request
from source import Minesweeper
import json

app = Flask(__name__)
app.secret_key = 'this is a secret key'

game = Minesweeper('medium')


# TODO: Add timer functions
def templating(the_game):
    rows = columns = the_game.play_field()
    return render_template('index.html',
                           rows=rows, columns=columns,
                           difficulty=game.difficulty,
                           num_of_flags=the_game.mines,
                           mine_locations=the_game.mine_locations,
                           ind_locations=the_game.ind_location,
                           ind_number=the_game.ind_number,
                           revealed_tiles=the_game.revealed_tiles,
                           start_tile=game.start_tile,
                           game_started=the_game.is_started)


@app.route('/')
def index():
    rows = columns = game.play_field()
    return render_template('index.html',
                           rows=rows,
                           columns=columns,
                           difficulty=game.difficulty,
                           num_of_flags=game.mines,
                           start_tile=game.start_tile,
                           game_started=game.is_started)
    # return templating(game)


@app.route('/', methods=['POST', 'GET'])
def form_post():
    if request.method == 'POST':
        keys = []
        for key in request.form.keys():
            keys.append(key)
        if 'difficulty' in keys:
            game.change_difficulty(request.form['difficulty'])
            return templating(game)
        if 'tile' in keys:
            tile = request.form['tile']
            print(tile)
            location = [int(x) for x in tile.split()]
            if [location[0], location[1]] not in game.mine_locations:
                # print("revealed 1:", game.revealed_tiles)
                game.reveal_tiles(location[0], location[1])
                # print("revealed 2:", game.revealed_tiles)
                revealed_ind_location, revealed_ind_number = game.get_revealed_indicators()
                data = {
                    "revealed_tiles": game.revealed_tiles,
                    "ind_location": revealed_ind_location,
                    "ind_number": revealed_ind_number
                }
                return json.dumps(data)
            else:
                print("game over")
                data = {
                    "game_over": "Game Over",
                    "mine_locations": game.mine_locations
                }
                return json.dumps(data)
        if 'new_game' in keys:
            game.new_game()
            return templating(game)
        if 'start_game' in keys:
            tile = request.form['start_game']
            location = [int(x) for x in tile.split()]
            game.start_game(location[0], location[1])
            revealed_ind_location, revealed_ind_number = game.get_revealed_indicators()
            data = {
                "start_game": [game.start_tile],
                "ind_location": revealed_ind_location,
                "ind_number": revealed_ind_number
            }
            return json.dumps(data)
            # return templating(game)
        if 'game_over' in keys:
            return '', 204  # HTTP empty response
        if 'test_key' in keys:
            test2 = {
                "mine_locations": game.mine_locations
            }
            mine_locations = game.mine_locations

            print("mine_locations:", mine_locations)
            return json.dumps(test2)
            # return jsonify(test2)
