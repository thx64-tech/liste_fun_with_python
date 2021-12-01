#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import EllipsisType


menu = [
    "Choissez parmi les 5 options suivantes :", 
    "1: Ajouter un élément à la liste", 
    "2: Retirer un élément de la liste", 
    "3: Afficher la liste", 
    "4 :Vider la liste", 
    "5: Quitter"
    ]

def affiche_menu():
    for entry in range(len(menu)):
        print(menu[entry])
    return int(input("Votre choix : "))

choix = affiche_menu()
liste = []
while choix != 5:
    match choix:
        case 1:
            element = input("Entrer un élément : ")
            liste.append(element) 
        case 2:
            schoix = int(input("Quel élément retirer : "))
            liste.pop(schoix)
        case 3:
            print(liste)
        case 4:
            liste.clear()
        case "5":
            break
    choix = affiche_menu()
    

