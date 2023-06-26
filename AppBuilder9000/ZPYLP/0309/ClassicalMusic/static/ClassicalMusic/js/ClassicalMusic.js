


$('#confirm_delete_pk').on('show.bs.modal', function (event) {
    var href_link = $(event.relatedTarget).data('val1');
    var item = $(event.relatedTarget).data('modal_body_text');

    $(this).find(".delete_link").attr("action", href_link);
    $(this).find(".modal-body").text(item);
});


function page_number_validate() {
    var page_selected = document.getElementById("page").value;
    var page_min = 1;
    var page_max = parseInt(document.getElementById("page").getAttribute("max"));
    if ((page_selected >= page_min) && (page_selected<=page_max)) {
        document.getElementById("page_number").submit()
    }
}

function show_table() {
  try {
    var x = document.getElementById("sort-table_wrapper");
    x.style.display = "block";
  }
  catch (e) {}
  try {
      var y = document.getElementById("table");
      y.style.display = "block";
  }
  catch (e) {}
  var z = document.getElementById("gallery");
  z.style.display = "none";
}

function show_gallery() {
  try {
      var x = document.getElementById("sort-table_wrapper");
      x.style.display = "none";
  }
  catch (e) {}
  try {
      var x = document.getElementById("table");
      x.style.display = "none";
  }
  catch (e) {}
  var x = document.getElementById("gallery");
  x.style.display = "flex";
}



function next_form(current) {
  current_form = "form-part" + current;
  var x = document.getElementById(current_form);
  x.style.display = "none";

  next = parseInt(current) +1;
  next_form = "form-part" + next;
  var y = document.getElementById(next_form);
  y.style.display = "inline-block";
}

function previous_form(current) {
  current_form = "form-part" + current;
  var x = document.getElementById(current_form);
  x.style.display = "none";

  next = parseInt(current) -1;
  next_form = "form-part" + next;
  var y = document.getElementById(next_form);
  y.style.display = "inline-block";
}





$(function () {
    var letters = $('.alphabet > a');
    var contentRows = $('#table table tbody tr');
    var contentCards = $('#gallery .gallery-container .musician-container');

    letters.not(':first').css('opacity','0.5');
    contentRows.each(function(){
        var sort_name = $(this).children('td:first').children('span').text().toUpperCase().trim();
        $('.alphabet a:eq('+(sort_name.charCodeAt(0)-64)+')').css('opacity','1.0');
    });

    letters.click(function () {
        var letter = $(this), text = $(this).text();
        if(text == 'All') text = '';

        letters.removeClass("active");
        letter.addClass("active");

        contentRows.hide();
        contentRows.each(function (i) {
            var cellText = $(this).children('td').children('span').eq(0).text();
            if (RegExp('^' + text).test(cellText.toUpperCase())) {
                $(this).fadeIn(400);
            }
        });

        contentCards.hide();
        contentCards.each(function (i) {
            var cellText = $(this).children('a').children('span').eq(0).text();
            if (RegExp('^' + text).test(cellText.toUpperCase())) {
                $(this).fadeIn(400);
            }
        });
    });
});

$(document).ready( function () {
    $('#sort-table').DataTable();
} );