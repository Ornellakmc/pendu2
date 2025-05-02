import random

# Fonction qui affiche les différentes étapes du pendu en fonction du nombre d'erreurs
def dessinPendu(nb):
    tab = [
        """
           +-------+
           |
           |
           |
           |
           |
        ==============
        """,
        """
           +-------+
           |       |
           |       O
           |
           |
           |
        ==============
        """,
        """
           +-------+
           |       |
           |       O
           |       |
           |
           |
        ==============
        """,
        """
           +-------+
           |       |
           |       O
           |      -|
           |
           |
        ==============
        """,
        """
           +-------+
           |       |
           |       O
           |      -|-
           |
           |
        ==============
        """,
        """
           +-------+
           |       |
           |       O
           |      -|-
           |      |
           |
        ==============
        """,
        """
           +-------+
           |       |
           |       O
           |      -|-
           |      | |
           |
        ==============
        """
    ]
    return tab[nb]

# Fonction qui charge une liste de mots à partir d'un fichier texte
def liste_de_mots():
    l = []
    with open("tous_les_mots.txt", "r") as fichier:
        for i in fichier:
            l.append(i.strip())
    return l

# Fonction qui choisit un mot au hasard parmi la liste
def choisir_hasard(fichier):
    return random.choice(fichier).upper()

# Fonction principale du jeu du pendu
def jeu_pendu():
    while True:  # Cette boucle permet de rejouer si le joueur le souhaite
        mots = liste_de_mots()  # Récupère la liste de mots à partir du fichier
        mot_a_deviner = choisir_hasard(mots)  # Choisit un mot au hasard dans la liste
        lettres_trouvees = []  # Liste des lettres trouvées dans le mot
        lettres_envoyees = []  # Liste des lettres déjà essayées par le joueur
        essais_restants = 6  # Nombre d'erreurs autorisées

        print('Bienvenue au jeu du pendu !')
        print(dessinPendu(0))  # Affiche la première étape du pendu (aucune erreur)
        
        while essais_restants > 0:
            # Affichage du mot avec les lettres devinées et des '*' pour celles non trouvées
            affichage_mot = ' '.join([lettre if lettre in lettres_trouvees else '*' for lettre in mot_a_deviner])
            print('Mot à deviner :', affichage_mot)
            print('Lettres essayées :', ', '.join(lettres_envoyees))

            # Demande une lettre à l'utilisateur
            lettre = input('Proposez une lettre : ').upper()

            # Vérification de la validité de la lettre entrée
            if len(lettre) != 1 or not lettre.isalpha():  # isalpha vérifie si c'est bien une lettre
                print('Veuillez entrer une seule lettre.')
                continue

            # Vérification si la lettre a déjà été proposée
            if lettre in lettres_envoyees:
                print('Vous avez déjà essayé cette lettre.')
                continue

            lettres_envoyees.append(lettre)  # Ajoute la lettre à la liste des lettres essayées

            # Vérification si la lettre est dans le mot à deviner
            if lettre in mot_a_deviner:
                lettres_trouvees.append(lettre)  # Ajoute la lettre aux lettres trouvées
                print('Bonne lettre !')
            else:
                essais_restants -= 1  # Diminue le nombre de tentatives restantes
                print('Mauvaise lettre !')

            print(dessinPendu(6 - essais_restants))  # Met à jour le dessin du pendu

            # Ajout d'indications à partir de la quatrième tentative, mais pas quand il reste une seule lettre
            if essais_restants == 3 and len(set(mot_a_deviner) - set(lettres_trouvees)) > 1:  # Plus d'une lettre à deviner
                indication = input('Voulez-vous une indication ? (oui/non) : ').lower() #dmd au joueur si il veut une indiation lower met en minuscule
                if indication == 'oui':
                    lettre_indication = random.choice([lettre for lettre in mot_a_deviner if lettre not in lettres_trouvees])
                    print('Voici une indication : La lettre', lettre_indication, 'fait partie du mot.')

            # Vérifie si toutes les lettres du mot ont été trouvées
            if all(l in lettres_trouvees for l in mot_a_deviner):
                print('Félicitations ! Vous avez deviné le mot :', mot_a_deviner)
                break

        else:
            # Si le joueur n'a plus d'essais, il perd la partie
            print('Dommage ! Le mot était :', mot_a_deviner)

        # Demande au joueur s'il veut rejouer, peu importe s'il a gagné ou perdu
        rejouer = input('Voulez-vous rejouer ? (oui/non) : ').lower()
        if rejouer != 'oui':
            print("Merci d'avoir joué !")
            break  # Quitte la fonction et termine le jeu

# Lancement du jeu
jeu_pendu()
