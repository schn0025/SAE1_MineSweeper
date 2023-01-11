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
        raise TypeError(
            f"construireGrilleDemineur : Le nombre de lignes {nbLigne} ou de colonnes {nbCol} n’est pas un entier.")
    if nbLigne <= 0 or nbCol <= 0:
        raise ValueError(
            f"construireGrilleDemineur : Le nombre de lignes {nbLigne} ou de colonnes {nbCol} est négatif ou nul.")
    grille = []
    for i in range(nbLigne):
        ligne = []
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
    nbLigne = len(grille)
    return nbLigne


def getNbColonnesGrilleDemineur(grille: list) -> int:
    """
    renvoi le nombre de collone de la grille
    :param grille: grille de demineur
    :return: le nombre de collone de la grille
    """
    if not type_grille_demineur(grille):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    nbCol = len(grille[0])
    return nbCol


def isCoordonneeCorrecte(grille: list, co: tuple) -> bool:
    """
    recheche ci les coordonnée sont bien dans la grille
    :param grille: grille du demineur
    :param co: coordonnée recherche dans la grille
    :return: True ci les coordonnée sont dans la grille false sinon
    """
    if not type_grille_demineur(grille) or not type_coordonnee(co):
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    ligne = getLigneCoordonnee(co)
    col = getColonneCoordonnee(co)
    return ligne < getNbLignesGrilleDemineur(grille) and ligne >= 0 and col < getNbColonnesGrilleDemineur(
        grille) and col >= 0


def getCelluleGrilleDemineur(grille: list, co: tuple) -> dict:
    """
    cheche la cellule au coordonnée donnée et la renvoi
    :param grille: grille: grille du demineur
    :param co: coordonnée recherche dans la grille
    :return: la cellule au coordonnée données
    """
    if not type_grille_demineur(grille) and not isCoordonneeCorrecte(grille, co) and not type_coordonnee(co):
        raise TypeError(f"getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    ligne = getLigneCoordonnee(co)
    col = getColonneCoordonnee(co)
    cellule = grille[ligne][col]
    return cellule


def getContenuGrilleDemineur(grille: list, co: tuple) -> int:
    """
    return le contenus de la cellule au coordonnée passer en paramètre
    :param grille: grille du demineur
    :param co: coordonnée recherche dans la grille
    :return: le contenus de la cellule au coordonnée passer en paramètre
    """
    cellule = getCelluleGrilleDemineur(grille, co)
    return getContenuCellule(cellule)


def setContenuGrilleDemineur(grille: list, co: tuple, contenu) -> None:
    """
    modifie le contenu de la cellule au coordonnée passer en paramètre
    :param grille: grille du demineur
    :param co: coordonnée recherche dans la grille
    :param contenu: le contenus que l'on doit remplacer
    """
    cellule = getCelluleGrilleDemineur(grille, co)
    setContenuCellule(cellule, contenu)
    return None


def isVisibleGrilleDemineur(grille: list, co: tuple) -> bool:
    """
    indique ci la cellule au coordonnée passer en paramètre est visible ou non
    :param grille: grille du demineur
    :param co: coordonnée recherche dans la grille
    """
    cellule = getCelluleGrilleDemineur(grille, co)
    return isVisibleCellule(cellule)


def setVisibleGrilleDemineur(grille: list, co: tuple, visibili: bool) -> None:
    """

    :param grille: grille du demineur
    :param co: coordonnée recherche dans la grille
    :param visibili: visibilité de la celule
    """
    cellule = getCelluleGrilleDemineur(grille, co)
    setVisibleCellule(cellule, visibili)
    return None


def contientMineGrilleDemineur(grille: list, co: tuple) -> bool:
    """
    detecte la presence d'une mine dans la cellule placer au coordonnée passer en paramètre
    :param grille: grille du demineur
    :param co: coordonnée recherche dans la grille
    :return: True si il y a une bombe dans la cellule et false sinon
    """
    return getContenuGrilleDemineur(grille, co) == const.ID_MINE


def getCoordonneeVoisinsGrilleDemineur(grille: list, co: tuple) -> list:
    """
    cherche les co des voisin de la cos passer en paramètre
    :param grille: grille du demineur
    :param co: coordonnée dans la grille
    :return: la liste des voissin de la co passer en paramètre
    """
    if not type_grille_demineur(grille) and not isCoordonneeCorrecte(grille, co):
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type")
    if not isCoordonneeCorrecte(grille, co):
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")
    lstVoisin = []
    ligne = getLigneCoordonnee(co)
    col = getColonneCoordonnee(co)
    for y in range(-1, 2):
        coTemp = ((ligne - 1), (col + y))
        if type_coordonnee(coTemp):
            if isCoordonneeCorrecte(grille, coTemp):
                lstVoisin.append(coTemp)

    for y in range(-1, 2, 2):
        coTemp = (ligne, (col + y))
        if type_coordonnee(coTemp):
            if isCoordonneeCorrecte(grille, coTemp):
                lstVoisin.append(coTemp)

    for y in range(-1, 2):
        coTemp = ((ligne + 1), (col + y))
        if type_coordonnee(coTemp):
            if isCoordonneeCorrecte(grille, coTemp):
                lstVoisin.append(coTemp)
    return lstVoisin


def placerMinesGrilleDemineur(grille: list, nb: int, co: tuple) -> None:
    """
    place nb mine aleatoirement
    :param grille: grille du demineur
    :param nb: nombre de mines a placer
    :param co: coordonnée d'une cellule dans la grille qui ne doit pas être une mine
    """
    ligneMax = getNbLignesGrilleDemineur(grille) - 1
    colMax = getNbColonnesGrilleDemineur(grille) - 1
    if nb < 0 or nb >= ((ligneMax + 1) * (colMax + 1)):
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")

    if not type_coordonnee(co) or not isCoordonneeCorrecte(grille, co):
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille")

    nbMinePlace = 0

    while nbMinePlace < nb:
        col = randint(0, colMax)
        ligne = randint(0, ligneMax)
        coTemp = (ligne, col)
        if coTemp != co and getContenuGrilleDemineur(grille, coTemp) != const.ID_MINE:
            setContenuGrilleDemineur(grille, coTemp, const.ID_MINE)
            nbMinePlace += 1
    compterMinesVoisinesGrilleDemineur(grille)


def compterMinesVoisinesGrilleDemineur(grille: list) -> None:
    """
    compt les bombe sur les cases voisinne
    :param grille: grille du demineur
    """
    nbLigne = getNbLignesGrilleDemineur(grille)
    nbCol = getNbColonnesGrilleDemineur(grille)
    for ligne in range(nbLigne):
        for col in range(nbCol):
            co = (ligne, col)
            if getContenuGrilleDemineur(grille, co) != const.ID_MINE:
                voisins = getCoordonneeVoisinsGrilleDemineur(grille, co)
                nbMine = 0
                for voisin in voisins:
                    if getContenuGrilleDemineur(grille, voisin) == const.ID_MINE:
                        nbMine += 1
                setContenuGrilleDemineur(grille, co, nbMine)


def getNbMinesGrilleDemineur(grille: list) -> int:
    """
    compt le nombre de mine restant sur le demineur
    :param grille: grille du demineur
    :return: le nombre de mine restante
    """
    if not type_grille_demineur(grille):
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n’est pas une grille")
    nbMine = 0
    nbLigne = getNbLignesGrilleDemineur(grille)
    nbCol = getNbColonnesGrilleDemineur(grille)
    for ligne in range(nbLigne):
        for col in range(nbCol):
            co = (ligne, col)
            if getContenuGrilleDemineur(grille, co) == const.ID_MINE:
                nbMine += 1
    return nbMine


def getAnnotationGrilleDemineur(grille: list, co: tuple) -> str:
    """
    cherche l'annotation d'une cellule a partire d'une grille et d'une co
    :param grille: grille du demineur
    :param co: coordonnée d'une cellule dans la grille qui ne doit pas être une mine
    :return: l'annotation trouver
    """
    cel = getCelluleGrilleDemineur(grille, co)
    anot = getAnnotationCellule(cel)
    return anot
