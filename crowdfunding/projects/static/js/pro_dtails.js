var postbtn=document.getElementById("postcomment")
var mycomment=document.getElementById("comment")

var commentsdiv=document.getElementById("2a")



postbtn.addEventListener("click",function(){
    var myform=document.createElement('FORM');
    myform.setAttribute("method","post")

    var h3Tag = document.createElement('H3');


     
     var userdiv=document.createElement('DIV');

    var spanBy = document.createElement('SPAN');
    spanBy.innerHTML="By: "
    var spanuser = document.createElement('SPAN');
    // user name
    spanuser.innerHTML="mostafa"   

    userdiv.appendChild(spanBy)
    userdiv.appendChild(spanuser)
    userdiv.setAttribute("class","my-3")







    h3Tag.style.color="white"
    h3Tag.innerHTML = mycomment.value;

    var mydiv=document.createElement('DIV');
    var mylink=document.createElement('A');
    

    var Mybutton=document.createElement('BUTTON');
    Mybutton.innerHTML="Report"
    Mybutton.setAttribute("class","btn");
    Mybutton.setAttribute("class","p-3");
    Mybutton.setAttribute("type","button");


    mylink.setAttribute("href","./Commentreport.html")
    mylink.appendChild(Mybutton)







    Mybutton.setAttribute("class","btn-danger");
    myform.appendChild(h3Tag)
    myform.appendChild(userdiv)
    myform.appendChild(mylink)
    mydiv.appendChild(myform)


    commentsdiv.appendChild(mydiv)








})

function updte_Donate(){
    var Donated_Value = document.getElementById("Donate_input").value
    
    if(Donated_Value==0 || Donated_Value==""){
        document.getElementById('alert').style.display="";

        document.getElementById('alert').innerHTML = "please Enter Valid Donate"

    }else{
        document.getElementById('alert').style.display="none";
        var Donated_Value = parseFloat(document.getElementById("Donate_input").value)
        var data=document.getElementById('update_h3').innerHTML.split(" ");
        var newarray=data[0].split("$")
        var final_donated_value=Donated_Value+parseFloat(newarray[1])
        console.log(final_donated_value)
        document.getElementById('update_h3').innerHTML = "$"+final_donated_value+" USD";


    }
  }


  function validate_rate(){

    var Donated_Rate = document.getElementById("Donate_rate").value
    
    if(  Donated_Rate=="" || Donated_Rate<0 || Donated_Rate>10 ){
        document.getElementById('alertRate').style.display="";
        document.getElementById('alertRate').innerHTML = "please Enter Valid Rate between 1 to 10 "
    }else{
        document.getElementById('alertRate').style.display="none";
        Donated_Rate=document.getElementById("Donate_rate").value
        console.log(Donated_Rate)


    }
    
  }