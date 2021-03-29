from flask import Flask, render_template, request
from source import Minesweeper
import json

app = Flask(__name__)
app.secret_key = 'this is a secret key'

game = Minesweeper('medium')


# TODO: add modals (winner_winner and game_over)
#   https://www.w3schools.com/js/js_popup.asp
# TODO: Clean up code

def templating(the_game):
    rows = columns = the_game.play_field()
    return render_template('index.html',
                           rows=rows,
                           columns=columns,
                           difficulty=game.difficulty,
                           num_of_flags=the_game.mines)


@app.route('/')
def index():
    return templating(game)


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
            location = [int(x) for x in tile.split()]
            if [location[0], location[1]] not in game.mine_locations:
                game.reveal_tiles(location[0], location[1])
                revealed_ind_location, revealed_ind_number = game.get_revealed_indicators()
                if game.chicken_dinner() == "Winner Winner":
                    data = {
                        "Winner_Winner": "Chicken Dinner",
                        "revealed_tiles": game.revealed_tiles,
                        "ind_location": revealed_ind_location,
                        "ind_number": revealed_ind_number
                    }
                else:
                    data = {
                        "revealed_tiles": game.revealed_tiles,
                        "ind_location": revealed_ind_location,
                        "ind_number": revealed_ind_number
                    }
                return json.dumps(data)
            else:
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
                "revealed_tiles": game.revealed_tiles,
                "ind_location": revealed_ind_location,
                "ind_number": revealed_ind_number
            }
            return json.dumps(data)
        if 'game_over' in keys:
            return '', 204  # HTTP empty response
