print('Donnez votre nom')
nom = input()
print('Donnez votre prenom')
prenom = input()
print('Donnez age')
age = int(input())

if age == 9 or age == 10:
    print('Poussin')
elif age == 11 or age == 12:
    print('Benjamin')
elif age == 13 or age == 14:
    print('Minime')
elif age == 15 or age == 16:
    print('Cadet')
elif age == 17 or age == 18:
    print('Junior')
elif age >= 19 and age <= 34:
    print('Senior')
elif age >= 35:
    print('Veteran')
else:
    print('vous etes trop jeune')

