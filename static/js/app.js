function rightClick(clickEvent) {
    clickEvent.preventDefault();
}
// Disables right-clicking on webpage
document.oncontextmenu = rightClick;

// Color codes for mine indicators:
var indicator_style = {
    1: "#0000FF",  // Blue
    2: "#5cb85c",  // Green
    3: "#ff0000",  // Red
    4: "#800080",  // Purple
    5: "#800000",  // Maroon
    6: "#30D5C8",  // Turquoise
    7: "#000000",  // Black
    8: "#808080",  // Gray
}
function start_game(button_name, button_value, button_id) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var item = this.responseText;
            var item_parsed = JSON.parse(item);
            if ('start_game' in item_parsed) {
                var tile_nodes = document.getElementsByName("start_game");
                var tile_array = Array.prototype.slice.call(tile_nodes);
                for (let i = 0; i < tile_array.length; i++) {
                    tile_array[i].name = "tile";
                    tile_array[i].className = "btn btn-success square-button border d-inline";
                }
            }
            reveal_tiles(item_parsed)
            document.getElementById(button_id).style.backgroundColor = "#C4A484";
        }
    }
    xhttp.open("POST", "http://127.0.0.1:5000/", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(button_name + "=" + button_value);
    startTimer();
}
function WhichButton(event, button_name, button_value, button_id) {
    if (event.button == 0) {
        if (button_name == "start_game") {
            start_game(button_name, button_value, button_id);
        } else if (button_name == "tile") {
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    var item = this.responseText;
                    var item_parsed = JSON.parse(item);
                    var item_key = Object.keys(item_parsed);

                    reveal_tiles(item_parsed)

                    if ("game_over" in item_parsed) {
                        if ("mine_locations" in item_parsed) {
                            var mine_locations = item_parsed["mine_locations"];
                            for (let i = 0; i < mine_locations.length; i++) {
                                document.getElementById(mine_locations[i]).className = "btn square-button border d-inline bg-danger";
                            }
                        }
                        var tile_nodes = document.getElementsByName("tile");
                        var tile_array = Array.prototype.slice.call(tile_nodes);
                        for (let i = 0; i < tile_array.length; i++) {
                            tile_array[i].name = "game_over";
                        }
                        stopTimer();
                        alert("Game Over\n\nTo start a new game:\nChoose difficulty");
                        //send_message()
                    }
                    if ("Winner_Winner" in item_parsed) {
                        var tile_nodes = document.getElementsByName("tile");
                        var tile_array = Array.prototype.slice.call(tile_nodes);
                        for (let i = 0; i < tile_array.length; i++) {
                            tile_array[i].name = "winner_winner";
                        }
                        stopTimer();
                        alert("Winner Winner!\n\nTo start a new game:\nChoose difficulty");
                        //send_message()
                    }
                }
            };
            xhttp.open("POST", "http://127.0.0.1:5000/", true);
            xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhttp.send(button_name + "=" + button_value);
        }
    }
    else if (event.button == 2) {
        if (button_name != "start_game"){
            var flags_remaining = document.getElementById("num_of_flags_remaining").innerHTML;
            var flag_icon = "<i class='fa fa-flag fa-1x text-dark'></i>";

            // if (tile..style.backgroundColor != "#C4A484"){
            if (document.getElementById(button_id).name == "flagged") {
                document.getElementById(button_id).name = "tile";
                document.getElementById(button_id).innerHTML = "";
                document.getElementById("num_of_flags_remaining").innerHTML = parseInt(flags_remaining) + 1;
            }
            else {
                document.getElementById(button_id).innerHTML = flag_icon;
                document.getElementById(button_id).name = "flagged"
                document.getElementById("num_of_flags_remaining").innerHTML = parseInt(flags_remaining) - 1;
            }
        }
    }
}
var duration = document.getElementById("timer"),
    seconds = 0, minutes = 0,
    t;

function add() {
    seconds ++;
    if (seconds >= 60) {
        seconds = 0;
        minutes++;
    }
    duration.textContent = (minutes ? (minutes > 9 ? minutes : "0" + minutes) : "00") + ":" + (seconds > 9 ? seconds : "0" + seconds);
    timer();
}
function timer() {
    t = setTimeout(add, 1000);
}

function startTimer() {
    timer();
}
function stopTimer() {
    clearTimeout(t);
}
function send_message() {
    var r = confirm("Press a button!");
    if (r == true) {
    txt = "You pressed OK!";
    send_request();
    } else {
    txt = "You pressed Cancel!";
    }
}
function reveal_tiles(item_parsed) {
    if ("revealed_tiles" in item_parsed) {
        var value = item_parsed["revealed_tiles"];
        for (let i=0; i < value.length; i++) {
                document.getElementById(value[i]).className = "btn square-button border d-inline font-weight-bold";
                document.getElementById(value[i]).style.backgroundColor = "#C4A484";
        }
    }
    if ("ind_location" in item_parsed) {
        var ind_locations = item_parsed["ind_location"];
        if ("ind_number" in item_parsed) {
            var ind_number = item_parsed["ind_number"];
            for (let i = 0; i < ind_number.length; i++) {
                document.getElementById(ind_locations[i]).innerHTML = ind_number[i];
                document.getElementById(ind_locations[i]).style.color = indicator_style[ind_number[i]];
            }
        }
    }
}