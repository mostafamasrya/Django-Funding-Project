var deletep=document.getElementById("delete")

var namediv=document.getElementById("username")
var confirmdiv=document.getElementById("confirm")

var nobtn=document.getElementById("no")





deletep.addEventListener("click",function(){
    confirmdiv.style.display="block"
})


nobtn.addEventListener("click",function(){
    confirmdiv.style.display="none"

})




// handling log out 



var loglink=document.getElementById("loglink")
var logoutdiv=document.getElementById("logoutdiv")

var nolog=document.getElementById("nolog")


loglink.addEventListener("click",function(){
    logoutdiv.style.display="block"
})


nolog.addEventListener("click",function(){
    logoutdiv.style.display="none"

})



