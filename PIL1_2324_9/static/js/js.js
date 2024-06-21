
    var close1, close2,pop1,pop2,pop,ins,con;
    close1=document.querySelector('.close1')
    close2=document.querySelector('.close2')
    pop=document.querySelector('.popup-container')
    pop1=document.querySelector('.popup1')
    pop2=document.querySelector('.popup2')
    ins=document.querySelectorAll('.signup-button')
    con=document.querySelectorAll('.login-button')
     // Fonction pour afficher les pop-ups
     function showPopup(popup) {
        pop.style.display = 'flex'; // Affiche le conteneur de pop-up
        popup.style.display = 'block'; // Affiche le pop-up spécifié
    }

    // Fonction pour fermer les pop-ups
    function closePopup() {
        pop.style.display = 'none'; // Cache le conteneur de pop-up
        pop1.style.display = 'none'; // Cache le pop-up d'inscription
        pop2.style.display = 'none'; // Cache le pop-up de connexion
    }

    {/* // Événements pour ouvrir les pop-ups */}
    ins.forEach(function(button) {
        button.addEventListener('click', function() {
            showPopup(pop1); // Affiche le pop-up d'inscription
        });
    });
    
    con.forEach(function(button) {
        button.addEventListener('click', function() {
            showPopup(pop2); // Affiche le pop-up d'inscription
        });
    });
    

    {/* // Événements pour fermer les pop-ups */}
close1.addEventListener('click', closePopup);
close2.addEventListener('click', closePopup);