let isLastItemShowed = false;

// Fonction verifiant si l'input est rempli pour passer à l'étape d'après.
function nextStep(currentDiv, nextDiv, isThisTheLastItem = false){
    let divToHide = document.getElementById(currentDiv);
    let divToShow = document.getElementById(nextDiv);

    // Verification si l'input est vide
    for (let element of divToHide.childNodes){
        if (element.firstChild && element.firstChild.nodeName === 'INPUT'){ // Vérification si il y a un input.
            if (!element.firstChild.value){ // Vérification de si l'input est vide et si vide afficher pop-up
                document.getElementById("alert-field-empty").classList.add('is-active'); // Affichage de la pop-up
                return // Return pour ne pas continuer la procédure mais rester pour remplir l'input.
            }
        }
    }

    divToHide.style.display = "none"; // Cacher le div de l'étape actuelle
    divToShow.style.display = "block"; // Afficher le div de l'étape suivante

    if(isThisTheLastItem){
        isLastItemShowed = true;
    }
}


// Fonction servant à supprimer l'affichage d'une pop-up (modal bulma)
function closeModal(modalToClose){
    document.getElementById(modalToClose).classList.remove('is-active'); // Suppression de la pop-up
}