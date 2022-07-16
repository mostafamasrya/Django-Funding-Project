


var infolink=document.getElementById("infolink")
var camplink=document.getElementById("camplink")
var imgdiv=document.getElementById("myinfo")
var mycamp=document.getElementById("mycamp")


camplink.addEventListener("click",function(){
    mycamp.style.display="block"
    imgdiv.style.display="none"
})


infolink.addEventListener("click",function(){
    mycamp.style.display="none"
    imgdiv.style.display="block"
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