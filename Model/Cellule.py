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
    cette fonction verifie ci l'element dans la celule est corecte ou non
    :param elt: element contenu dans la celule
    :return bool: bool verifant la condition
    """
    rep = False
    if type(cont) == int:
        if (cont <= 8 and cont >= 0) or cont == const.ID_MINE:
            rep = True
    return rep

def construireCellule(cont: int= 0, visi: bool = False) -> dict:
    if not isContenuCorrect(cont):
        raise ValueError(f"construireCellule : le contenu {cont} n’est pas correct")

    if type(visi) != bool:
        raise TypeError( f"construireCellule : le second paramètre {type(visi)} n’est pas un booléen ")
    cel = {const.CONTENU: cont, const.VISIBLE: visi}
    return cel