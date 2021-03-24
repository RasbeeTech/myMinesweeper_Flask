from flask import Flask, render_template, request
from source import Minesweeper

app = Flask(__name__)
app.secret_key = 'this is a secret key'

game = Minesweeper('medium')

# TODO: Right Click actions:
#  https://stackoverflow.com/questions/51548401/how-to-send-out-an-ajax-request-to-flask
#  https://www.geeksforgeeks.org/how-to-add-a-custom-right-click-menu-to-a-webpage/
#  https://www.w3schools.com/xml/ajax_xmlhttprequest_send.asp
# TODO: Add timer functions
# TODO: Add function to decrement number of flags
# TODO: Setup flask to send responses to javascript code

indicator_style = {
    1: "color: #0000FF;",  # Blue
    2: "color: #5cb85c;",  # Green
    3: "color: #ff0000;",  # Red
    4: "color: #800080;",  # Purple
    5: "color: #800000;",  # Maroon
    6: "color: #30D5C8;",  # Turquoise
    7: "color: #000000;",  # Black
    8: "color: #808080;",  # Gray
}


def templating(the_game):
    rows = columns = the_game.play_field()
    return render_template('index.html',
                           rows=rows, columns=columns,
                           difficulty='medium',
                           num_of_flags=the_game.mines,
                           mine_locations=the_game.mine_locations,
                           ind_locations=the_game.ind_location,
                           ind_number=the_game.ind_number,
                           indicator_style=indicator_style,
                           revealed_tiles=the_game.revealed_tiles)


# TODO: render part of template instead of entire window
#  https://stackoverflow.com/questions/21515554/render-part-of-the-template-in-flask
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
            print(tile)
            location = [int(x) for x in tile.split()]
            game.reveal_tiles(location[0], location[1])
            # print(game.mine_locations)
            # print(game.revealed_tiles)
            return templating(game)
        if 'start_game' in keys:
            tile = request.form['start_game']
            location = [int(x) for x in tile.split()]
            game.start_game(location[0], location[1])
            return templating(game)
        if 'mine_tile' in keys:
            game.toggle_game_over()
            return '', 204  # HTTP empty response
        if 'new_game' in keys:
            # TODO: flask controlled Modal:
            #  https://stackoverflow.com/questions/54524827/how-to-show-bootstrap-modal-on-rendering-the-same-page-in-flask
            game.new_game()
            return templating(game)
