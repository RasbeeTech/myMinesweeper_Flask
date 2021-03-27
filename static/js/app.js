document.oncontextmenu = rightClick;

        function rightClick(clickEvent) {
            clickEvent.preventDefault();
        }

        var indicator_style = {
            1: "color: #0000FF;",  //Blue
            2: "color: #5cb85c;",  //Green
            3: "color: #ff0000;",  //Red
            4: "color: #800080;",  Purple
            5: "color: #800000;",  # Maroon
            6: "color: #30D5C8;",  # Turquoise
            7: "color: #000000;",  # Black
            8: "color: #808080;",  # Gray
        }

        function WhichButton(event, button_name, button_value, button_id) {
            if (event.button == 0) {
                alert("You pressed button event: " + event.button);
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
                                    //document.getElementById("test_paragraph2").innerHTML += value[i];
                                    document.getElementById(value[i]).className = "btn square-button border d-inline";
                                    document.getElementById(value[i]).style.backgroundColor = "#C4A484";
                                }
                        }
                        if ("ind_location" in item_parsed) {
                            var ind_locations = item_parsed["ind_location"];
                            if ("ind_number" in item_parsed) {
                                var ind_number = item_parsed["ind_number"];
                                for (let i = 0; i < ind_number.length; i++) {
                                    document.getElementById(ind_locations[i]).innerHTML = ind_number[i];
                                }
                            }
                        }
                        /*for (var key in item_parsed) {
                            if (key == "mine_locations") {
                                document.getElementById("test_paragraph").innerHTML = item_key[0];
                                document.getElementById("test_paragraph2").innerHTML = "values: ";

                                for (let i = 0; i < item_value.length; i++) {
                                    document.getElementById("test_paragraph2").innerHTML += item_value[i];
                                    document.getElementById(item_value[i]).className = "btn btn-warning square-button border d-inline";
                                }
                            }
                            if (key == "revealed_tiles") {
                                var value = item_parsed[key];

                                for (let i=0; i < value.length; i++) {
                                    //document.getElementById("test_paragraph2").innerHTML += value[i];
                                    document.getElementById(value[i]).className = "btn square-button border d-inline";
                                    document.getElementById(value[i]).style.backgroundColor = "#C4A484";
                                }
                            }
                        }*/
                    }
                };
                document.getElementById("test_paragraph3").innerHTML = button_name;

                xhttp.open("POST", "http://127.0.0.1:5000/", true);
                xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                var test_key = "test_key";
                var test_value = "test_value";
                //xhttp.send(test_key + "=" + test_value);
                xhttp.send(button_name + "=" + button_value);
            }
            else if (event.button == 2) {
                alert("You pressed button event: " + event.button);
                //alert("You pressed button name: " + button_name);
                //alert("You pressed button value: " + button_value);
                //alert("You pressed button id: " + button_id);

                var xhttp = new XMLHttpRequest();

                //xhttp.onreadystatechange = function() {
                //  if (this.readyState == 4 && this.status == 200) {
                //      document.getElementById("demo").innerHTML = this.responseText;
                //  }
                //};

                xhttp.open("POST", "http://127.0.0.1:5000/", true);
                xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhttp.send("tile="+button_value);


                var flags_remaining = document.getElementById("num_of_flags_remaining").innerHTML;
                var flag_icon = "<i class='fa fa-flag fa-1x text-dark'></i>";

                // Below if-statement does not work
                if (document.getElementById(button_id).innerHTML == flag_icon) {
                    document.getElementById(button_id).innerHTML = "";
                    document.getElementById("num_of_flags_remaining").innerHTML = parseInt(flags_remaining) + 1;
                }
                else {
                    document.getElementById(button_id).innerHTML = flag_icon;
                    document.getElementById("num_of_flags_remaining").innerHTML = parseInt(flags_remaining) - 1;
                }
                document.getElementById(button_id).innerHTML = flag_icon;
            }
        }