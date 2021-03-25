document.oncontextmenu = rightClick;

function rightClick(clickEvent) {
    clickEvent.preventDefault();
}

function WhichButton(event, button_name, button_value, button_id) {
    if (event.button == 0) {
        alert("You pressed button event: " + event.button);
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
              var item = this.responseText
              //var item = JSON.parse(items)
              //for (var key in item) {
              //  document.getElementById("test_paragraph").innerHTML = JSON.stringify(items, undefined, 2);
              //}
              if(typeof(item)== "string"){
                document.getElementById("test_paragraph").innerHTML = "string";
              }
          }
        };
        xhttp.open("POST", "http://127.0.0.1:5000/", true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("test_key=test_value");
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
        document.getElementById("num_of_flags_remaining").innerHTML = parseInt(flags_remaining) - 1;
        var flag_icon = "<i class='fa fa-flag fa-1x text-dark'></i>"
        document.getElementById(button_id).innerHTML = flag_icon;
    }

}