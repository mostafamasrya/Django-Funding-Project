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