function rightClick(clickEvent) {
    clickEvent.preventDefault();
}

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
function new_game(button_name, button_value) {
    //alert("button_name: " + button_name);
    //alert("button_value: " + button_value);
    $('#game-over-modal').modal('hide');
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://127.0.0.1:5000/", true);
    xhttp.send(button_name + "=" + button_value);
}
function start_game(button_name, button_value, button_id) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var item = this.responseText;
            var item_parsed = JSON.parse(item);
            //alert(item_parsed);
            if ('start_game' in item_parsed) {
                //alert("started");
                var tile_nodes = document.getElementsByName("start_game");
                var tile_array = Array.prototype.slice.call(tile_nodes);
                for (let i = 0; i < tile_array.length; i++) {
                    tile_array[i].name = "tile";
                    //tile_array[i].onmousedown = "WhichButton(event,this.name,this.value,this.id)";
                    tile_array[i].className = "btn btn-success square-button border d-inline";
                }
            }
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
            document.getElementById(button_id).style.backgroundColor = "#C4A484";
        }
    }
    xhttp.open("POST", "http://127.0.0.1:5000/", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(button_name + "=" + button_value);
}

function WhichButton(event, button_name, button_value, button_id) {
    if (event.button == 0) {
        if (button_name == "start_game") {
            start_game(button_name, button_value, button_id);
        } else if (button_name == "tile") {
            //alert("You pressed button event: " + event.button);
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    var item = this.responseText;
                    var item_parsed = JSON.parse(item);
                    var item_key = Object.keys(item_parsed);

                    var item_value = item_parsed[item_key[0]];

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
                        alert("Game Over");
                    }
                    if ("Winner_Winner" in item_parsed) {
                        var tile_nodes = document.getElementsByName("tile");
                        var tile_array = Array.prototype.slice.call(tile_nodes);
                        for (let i = 0; i < tile_array.length; i++) {
                            tile_array[i].name = "winner_winner";
                        }
                        alert("Winner Winner!");
                    }
                }
            };
            xhttp.open("POST", "http://127.0.0.1:5000/", true);
            xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            var test_key = "test_key";
            var test_value = "test_value";
            xhttp.send(button_name + "=" + button_value);
        }
    }
    else if (event.button == 2) {
        if (button_name != "start_game"){
            //alert("You pressed button event: " + event.button);

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
}document.oncontextmenu = rightClick;