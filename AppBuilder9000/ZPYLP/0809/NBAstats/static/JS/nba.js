

function sortTable(column) {
  var table, rows, switching, i, x, y, shouldSwitch;
  table = document.getElementById("myTable");
  switching = true;
  while (switching) {
    switching = false;
    rows = table.rows;
    // Loop through all table rows (except the
    // first, which contains table headers):
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      // Get the two elements you want to compare,
      // one from current row and one from the next:
      xString = rows[i].getElementsByTagName("TD")[column].innerHTML;
      yString = rows[i + 1].getElementsByTagName("TD")[column].innerHTML;
      x = parseInt(xString);
      y = parseInt(yString);
      //check if the two rows should switch place:
      if (x < y) {
        //if so, mark as a switch and break the loop:
        shouldSwitch = true;
        break;
      }
    }
    if (shouldSwitch) {
      // If a switch has been marked, make the switch
      // and mark that a switch has been done:
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    }
  }
}


function savePlayerFunc(key) {
    var element_table = document.getElementsByName('brTable');
    var element_tableRows = element_table[0].rows;
    var data = [];
    for(var i = 1 ; i < element_tableRows.length; i++)
    {
        data[i] = element_tableRows[i].getAttribute("name");
        dataString = String(data[i]); // convert row object to string
        dataKey = dataString.split(",")[0];
        if (dataKey == key) {
            dataArray = dataString.split(","); // convert string to array, separated by spaces
            playerName = dataArray[1];
            defRebs = dataArray[2];
            steals = dataArray[3];
            blocks = dataArray[4];
            total = dataArray[5];
            document.getElementById("playerName").innerHTML = playerName;
            document.getElementById("defRebs").innerHTML = defRebs;
            document.getElementById("steals").innerHTML = steals;
            document.getElementById("blocks").innerHTML = blocks;
            document.getElementById("total").innerHTML = total;
            break;
        }
    }
}

function showDiv() {
    var T = document.getElementById("show-div");
    T.style.display = "block";
}

function removeConfirm() {
    alert("Delete Player From Favorites?");
}
