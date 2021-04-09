
 function ageValidation()
{
     var x = document.getElementById("txtAge").value;
     if (x < 1 || x > 100)
     {
            alert("enter age between 1 to 100")
     }
}
function checkPassword(form) {
                password1 = form.password1.value;
                password2 = form.password2.value;

                // If password not entered
                if (password1 == '')
                    alert ("Please enter Password");

                // If confirm password not entered
                else if (password2 == '')
                    alert ("Please enter confirm password");

                // If Not same return False.
                else if (password1 != password2) {
                    alert ("\nPassword did not match: Please try again...")
                    return false;
                }

                // If same return True.
                else{
                    return true;
                }
            }
function validateemail()
{
var x=document.myform.email.value;
var atposition=x.indexOf("@");
var dotposition=x.lastIndexOf(".");
if (atposition<1 || dotposition<atposition+2 || dotposition+2>=x.length){
  alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);
  return false;
  }
}


