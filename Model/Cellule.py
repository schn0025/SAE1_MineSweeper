# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(cont: int) -> bool:
    """
    cette fonction verifie ci l'element dans la cellule est corecte ou non
    :param elt: element contenu dans la cellule
    :return bool: bool verifant la condition
    """
    rep = False
    if type(cont) == int:
        if (cont <= 8 and cont >= 0) or cont == const.ID_MINE:
            rep = True
    return rep

def construireCellule(cont: int= 0, visible: bool = False) -> dict:
    """
    cette fonction renvois un dictionaire de ce qui compose la cellule
    :param cont : le contenus de la cellule
    :param visi : un bool de ci le contenus de la celule est visible ou non
    :return le dictionaire avec les couple de valeurs
    """
    if not isContenuCorrect(cont):
        raise ValueError(f"construireCellule : le contenu {cont} n’est pas correct")

    if type(visible) != bool:
        raise TypeError( f"construireCellule : le second paramètre {type(visible)} n’est pas un booléen ")
    cel = {const.CONTENU: cont, const.VISIBLE: visible,const.ANNOTATION:None}
    return cel

def getContenuCellule(dico: dict) ->int:
    """
    renvoi le contenu de la cellule
    :param dico: un dico detaillent une cellule
    :return: le contenu de la cellule
    """
    if not type_cellule:
        raise TypeError(f"getContenuCellule : Le paramètre n’est pas une cellule")
    return dico[const.CONTENU]

def isVisibleCellule(dico:dict) ->bool:
    """
    renvoi la visibiliter de la cellule
    :param dico: un dico detaillent une cellule
    :return: la visibilité de ma celule
    """
    if not type_cellule:
        raise TypeError(f"isVisibleCellule : Le paramètre n’est pas une cellule")
    return dico[const.VISIBLE]

def setContenuCellule(dico: dict, cont: int)->None:
    """
    devinie le contenu d'une cellule au conteu passer en parametre
    :param dico: un dico detaillent une cellule
    :param cont: u contenu pour la cellule
    """
    if type(cont) != int:
        raise TypeError(f'setContenuCellule : Le second paramètre n’est pas un entier.')
    if not isContenuCorrect(cont):
        raise ValueError(f"setContenuCellule : la valeur du contenu {cont} n’est pas correcte.")
    if not type_cellule:
        raise TypeError(f"« setContenuCellule : Le premier paramètre n’est pas une cellule.")
    dico[const.CONTENU] = cont
    return None

def setVisibleCellule(dico:dict, visible: bool)-> None:
    """
    deffinie la visibiliter d'une celule a True
    :type dico: un dico detaillent une cellule
    """
    if not type_cellule:
        raise TypeError(f"setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if type(visible) != bool:
        raise TypeError(f'setVisibleCellule : Le second paramètre n’est pas un booléen.')
    dico[const.VISIBLE] = visible
    return None

def contientMineCellule(dico: dict)->bool:
    """
    renvoi un bool ci la cellule contient une mine ou non
    :param dico: un dico detaillent une cellule
    :return: True ci la cellule contient une mine False ci-non
    """
    if not type_cellule:
        raise TypeError(f"contientMineCellule : Le paramètre n’est pas une cellule.")
    rep = False
    if dico[const.CONTENU] == const.ID_MINE:
        rep = True
    return rep

def isAnnotationCorrecte(annotation: str) -> bool:
    """
    verifie ci le parametre est corecte
    :param annotation: annotation a verifier
    :return: True ci l'annotation est corecte False sinon
    """
    lstRep = [None, const.DOUTE, const.FLAG]
    return annotation in lstRep

def getAnnotationCellule(cel: dict) -> str:
    if not type_cellule(cel):
        raise TypeError(f" getAnnotationCellule : le paramètre {cel} n’est pas une cellule")
    rep = None
    if const.ANNOTATION in cel:
        rep = cel[const.ANNOTATION]
    return rep