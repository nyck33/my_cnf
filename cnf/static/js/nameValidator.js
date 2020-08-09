window.onload = function(){
    //don't use onclick, keep js in js
    var submit = document.getElementById("top-button");
    if(submit){
        submit.addEventListener("click", nameValidator);
    }
    //clear button
    var clear = document.getElementById("clear-button");
    if(clear){
        clear.addEventListener("click", reloader);
    }
            
    function nameValidator(){
        var x;
        var letters = (/^[a-zA-Z]+$/);
        
        //get val of input field with id="name"
        x = document.getElementById("nameInput").value;

        var currDiv = document.getElementById("topMsg");
       
        //check input
        if(letters.test(x)){
            //window.alert(x+', even if a 100% plant-based diet is out of reach, an "all or something" approach cuts through confusion, fusing cutting edge science'+
            //' with practical advice --from the Game Changers website');
            var a = document.createElement("a");
            var linkText = document.createTextNode("click here for quick and delicious Game Changers' Recipes");
            a.appendChild(linkText);
            a.id = "gcLink";
            a.title = "link to GC Recipes";
            a.href = "https://gamechangersmovie.com/food/";
            a.target = "_blank";
           
            currDiv.appendChild(a);
        }
        //non-alpha entry
        else{
            var newImg = document.createElement("img");
            newImg.class = "img-fluid img-responsive";
            newImg.id = "newImg";
            newImg.src = "https://nyck33.github.io/ecoWarriors/public/imgs/animals/polarbearCaption.jpg";
            currDiv.appendChild(newImg);
            
        }
        
    }

    function reloader(){
        var currLink = document.getElementById("gcLink");
        if(currLink){
            currLink.parentNode.removeChild(currLink);
        }
        var currImg = document.getElementById("newImg");
        if(currImg){
            currImg.parentNode.removeChild(currImg);
        }
        
    }
}
