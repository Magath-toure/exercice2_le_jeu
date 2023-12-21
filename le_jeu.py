
import random
nombre_aleatoire = random.randint(1, 100)
vie = 5
while True:
    choix_utilisateur = input("veuillez choir un chiffre entre 1 et 100 :")

    choix_utilisateur = int(choix_utilisateur)
    if choix_utilisateur == nombre_aleatoire:
        print("winner !.")
        break
        
    if vie == 0:
        print("fin du jeu! vous avez perdu",vie)
        break
    

    elif choix_utilisateur < nombre_aleatoire:
        print("c'est trop petit, une tentative en moins")
        vie -= 1
        print("une tentative en moins",vie)
    elif choix_utilisateur > nombre_aleatoire:
        print("c'est trop grand,une autre tentative en moins")
        vie -= 1
        print("une tentative en moins",vie)

    
   
    


                          

