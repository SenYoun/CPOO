import random

aleatoire = random.randint(0, 10)


for i in range(10):

    response = int(input("essayez de trouver le chiffre aleatoire : "))
    if response == aleatoire:
        print("Correct!")
        break
    else:
        print("Incorrect. Il vous reste", 9 - i, "tentatives.")
else:
    print("Vous avez épuisé toutes vos tentatives.")