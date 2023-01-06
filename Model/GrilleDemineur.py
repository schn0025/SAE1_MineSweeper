# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True

def construireGrilleDemineur(nbLigne: int, nbCol: int) -> list:
    """
    prend un nombre de ligne et de collone en parametre et renvoi une grille pour le demineur
    :param nbLigne: nombre de ligne voulu
    :param nbCol: nombre de collone voulu
    :return: la grille de dimension voulue
    """
    if type(nbLigne) != int or type(nbCol) != int:
        raise TypeError(f"construireGrilleDemineur : Le nombre de lignes {nbLigne} ou de colonnes {nbCol} n’est pas un entier.")
    if nbLigne <= 0 or nbCol <= 0:
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes {nbLigne} ou de colonnes {nbCol} est négatif ou nul.")
    grille=[]
    for i in range(nbLigne):
        ligne=[]
        for y in range(nbCol):
            cellule = construireCellule()
            ligne.append(cellule)
        grille.append(ligne)
    return grille

def getNbLignesGrilleDemineur(grille: list) -> int:
    """
    indique le nombre de ligne qui compose la grille
    :param grille: grille de demineur
    :return: nombre de ligne de la grille
    """
    if not type_grille_demineur(grille):
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    nbLigne= len(grille)
    return nbLigne

def getNbColonnesGrilleDemineur(grille: list)->int:
    """
    renvoi le nombre de collone de la grille
    :param grille: grille de demineur
    :return: le nombre de collone de la grille
    """
    if not type_grille_demineur(grille):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    nbCol=len(grille[0])
    return nbCol


def isCoordonneeCorrect(grille: list, co: tuple)-> bool:
    """
    recheche ci les coordonnée sont bien dans la grille
    :param grille: grille du demineur
    :param co: coordonnée recherche dans la grille
    :return: True ci les coordonnée sont dans la grille false sinon
    """
    if not type_grille_demineur(grille) or type(co) != tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    rep = False
    if co[0] < getNbLignesGrilleDemineur(grille) and co[0] > 0 and co[1] < getNbColonnesGrilleDemineur(grille) and co[1] > 0:
        rep = True
    return rep

def getCelluleGrilleDemineur(grille: list,co:tuple) -> dict:
    """
    cheche la cellule au coordonnée donnée et la renvoi
    :param grille: grille: grille du demineur
    :param co: coordonnée recherche dans la grille
    :return: la cellule au coordonnée données
    """
    if not type_grille_demineur(grille) and not isCoordonneeCorrect(grille,co) and type(co) != tuple:
        raise TypeError(f"getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    cellule = grille[co[0]][co[1]]
    return cellule
