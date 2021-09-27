#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        liste1 = []
        i = 0
        while i <10:
            i += 1
            valeur = input("Entrez une valeur")
            liste1.append (valeur)
            liste1.sort()
        return print (liste1)


def anagrams(words: list = None) -> bool:
    mot1 = input("Entrer votre mot")
    mot2 = input("Entrer le deuxième mot")
    listemot1 = []
    listemot2 = []
    for lettre1 in mot1:
        listemot1.append (lettre1)
        listemot1.sort()
    for lettre2 in mot2:
        listemot2.append (lettre2)
        listemot2.sort()
    if listemot2 == listemot1:
        return True
    else:
        return False

def contains_doubles(items: list) -> bool:
    
    for chiffre in items: 
        if items.count(chiffre) > 1:
            return(True)
        else:
            return (False)


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
