
import random
# ouvre le chemin du fichier spécifié en paramètre (dictionnaire.txt)
with open("dictionnaire.txt", "r") as f:
    ligne = f.readlines()

# variables globales
score = 0
lifs = 5
all_words = []
mot_a_deviner = ""
mot_aleatoire = ""

# fonctions du projet


def Mot():
    global mot_a_deviner, mot_aleatoire
    for i in ligne:
        lists = i.split(';')[0]
        all_words.append(lists)
    aleatoire = random.choice(all_words)
    mot_aleatoire = aleatoire
    for l in mot_aleatoire:
        mot_a_deviner += " _ "
    print('dans le fonc Mot :', mot_aleatoire)  # montrer la reponse
    print(f"mot à deviner a {len(mot_aleatoire)} lettre :", mot_a_deviner)


def rejouer():
    global lifs
    replay = input("vous voulez rejouer O/N ?")
    if replay == "O" or replay == "o":
        lifs = 5
        Start()
    if replay == "N" or replay == "n":
        exit()
    if replay == "*":
        print("le lettre saisi n'est pas reconnu")
        replay = input("vous voulez rejouer O/N ?")

# Fonction démarrant le programme Tire extensivement partie de la fonction pendu()


def Start():
    return Pendu()

# Fonction représentant le cœur de la logique du programme


def Pendu():
    global score, mot_aleatoire, mot_a_deviner, lifs
    lettre_trouve = ""
    Mot()

    while lifs > 0:
        lettre = input("entrer une lettre : ")

        if lettre in mot_aleatoire:
            mot_a_deviner = ""
            lettre_trouve += lettre
            for x in mot_aleatoire:
                if x in lettre_trouve:
                    mot_a_deviner += x
                else:
                    mot_a_deviner += " _ "
            print("bien vu !", mot_a_deviner)

        if mot_a_deviner == mot_aleatoire:
            score += 1
            mot_a_deviner = ""
            print("Bravo ! vous avez ", score, "score !")
            lifs = 0

        if lettre not in mot_aleatoire:
            lifs -= 1
            print("vous avez raté ! il vous rest ", lifs, "vies !")
        if lifs == 0:
            mot_a_deviner = ""
            print('le mot correct est :', mot_aleatoire, "!")
            rejouer()


# lancement du programme
Start()
