# générer un chiffre random entre 0 et 100
import random
numero_gagnant = int(random.randint(0,100))
print (numero_gagnant)


vie = 5

while True:

    if vie == 0:
        print("c'est perdu!!")
        break
    
    choix = input("quel est le numéro gagnant?")
    réponse_utilisateur = int(choix)        

    #dans le cas ou c'est gagné
    if réponse_utilisateur == numero_gagnant:
        print("vous avez gagné bien joué!!!")
        break

    # dans le cas ou c'est trop grand
    elif réponse_utilisateur > numero_gagnant:
        vie -= 1
        print("c'est moins et il vous reste ",vie, "vies!" ) 
       

    #dans le cas ou c'est plus
    elif réponse_utilisateur < numero_gagnant:
        vie -= 1
        print("c'est plus et il vous reste ",vie, "!" )
    
    




