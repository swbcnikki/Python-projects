//We'll use this file to confirm deletion of an entry!

function ConfirmDelete(pk) {
    var delete_confirmation = confirm("This is your final warning! Are you positive you want to delete this entry?");
    if (delete_confirmation == true) {
        window.location.href = "../../" + pk + "/deleteSuccess/";

        //Testing to make sure I can actually load another page with JS
        //window.location.href = "www.google.com"
    }
    else
    {
        alert("Your entry hasn't been deleted.")
    }


}