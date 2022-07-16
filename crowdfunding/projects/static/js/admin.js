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




document.querySelector("#exampleInputfile").addEventListener("change", (e) => { //CHANGE EVENT FOR UPLOADING PHOTOS
    if (window.File && window.FileReader && window.FileList && window.Blob) { //CHECK IF FILE API IS SUPPORTED
      const files = e.target.files; //FILE LIST OBJECT CONTAINING UPLOADED FILES
      const output = document.querySelector("#result2");
      output.innerHTML = "";
      for (let i = 0; i < files.length; i++) { // LOOP THROUGH THE FILE LIST OBJECT
          if (!files[i].type.match("image")) continue; // ONLY PHOTOS (SKIP CURRENT ITERATION IF NOT A PHOTO)
          const picReader = new FileReader(); // RETRIEVE DATA URI 
          picReader.addEventListener("load", function (event) { // LOAD EVENT FOR DISPLAYING PHOTOS
            const picFile = event.target;
            const div = document.createElement("div");
            div.innerHTML = `<img class="thumbnail" src="${picFile.result}" title="${picFile.name}"/>`;
            output.appendChild(div);
          });
          picReader.readAsDataURL(files[i]); //READ THE IMAGE
      }
    } else {
      alert("Your browser does not support File API");
    }
  });





  var proReportsDiv=document.getElementById("proReportsDiv")
  var commentsDiv=document.getElementById("commentsDiv")
  var projectsDiv=document.getElementById("projectsDiv")
var categoryDiv=document.getElementById("categoryDiv")







