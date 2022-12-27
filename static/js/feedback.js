
function validate()
{
    var flag = true;
    if(document.forms["feedback-box"]["user-name"].value == "" || document.forms["feedback-box"]["user-email"].value == "")
    {
        flag = false;
    }

    if(flag == false)
    {
        window.alert("Please fill all the details.");
    }
    else{
        window.alert("Submit Response?");
        
    }
}





