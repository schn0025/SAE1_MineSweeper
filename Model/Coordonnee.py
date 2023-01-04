# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0

def construireCoordonnee(num_ligne: int, num_colonne: int) -> tuple:
    """
    passe les parametre passer en argument sous la forme d'un tuple
    :param num_ligne: le numéro de ligne c’est-à-dire l’ordonnée y
    :param num_colonne: le numéro de la colonne, c’est-à-dire l’abscisse x
    :return: le tuple des coordonnées correspondant
    """
    if type(num_ligne) != int or type(num_colonne) != int:
        raise TypeError(f'construireCoordonnee : Le numéro de ligne {type(num_ligne)} ou le numéro de colonne {type(num_colonne)} ne sont pas des entiers')
    if num_ligne < 0 or num_colonne < 0:
        raise ValueError(f'construireCoordonnee : Le numéro de ligne {num_ligne} ou de colonne {num_colonne} ne sont pas positifs')
    return (num_ligne, num_colonne)

def getLigneCoordonnee(co: tuple) -> int:
    """
    retourne le numéro de colonne contenu dans
la coordonnée passée en paramètre
    :param co: coordonnée passer en paramètre
    :return: return la valeur de y
    """
    if type(co) != tuple:
        raise TypeError('getLigneCoordonnee : Le paramètre n’est pas une coordonnée')
    return co[0]

def getColonneCoordonnee(co: tuple) -> int:
    """
    retourne le numéro de colonne contenu dans
la coordonnée passée en paramètre
    :param co:coordonnée passer en paramètre
    :return: return la valeur de x
    """
    if type(co) != tuple:
        raise TypeError('getColonneCoordonnee : Le paramètre n’est pas une coordonnée')
    return co[1]