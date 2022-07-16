


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


// handling deleting account


// var deletep1=document.getElementById("delete1")

// var namediv1=document.getElementById("username")
// var confirmdiv1=document.getElementById("confirm1")

// var nobtn1=document.getElementById("no1")





// deletep1.addEventListener("click",function(){
//     confirmdiv1.style.display="block"
// })


// nobtn1.addEventListener("click",function(){
//     confirmdiv1.style.display="none"

// })