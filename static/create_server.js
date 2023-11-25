const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
if(urlParams.get('alert')){
    alert("Merci de remplir tout les champs requis!")
}

function nextStep(currentDiv, nextDiv){
    let divToHide = document.getElementById(currentDiv);
    let divToShow = document.getElementById(nextDiv);

    divToHide.style.display = "none";
    divToShow.style.display = "block";
}