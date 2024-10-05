""" travailler sur les fichiers """
#### Imports et définition des variables globales
import random
FILENAME = "listes.csv"

#### Fonctions secondaires
""" travailler sur les listes apporté par les fichiers"""
def read_data(filename):
    """retourne le contenu du fichier <filename>
    Args:
        filename (str): nom du fichier à lire
    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding='utf8') as file:
        # Utilise readlines() pour lire toutes les lignes du fichier
        r = file.readlines()

        # Pour chaque ligne, enlève les espaces inutiles et convertit les éléments en entier
        l = [list(map(int, line.split(';'))) for line in r]

    return l


def get_list_k(l,k):
    """retourne la kième liste
    Args: prend en argument la liste de listes retournée par read_data() et un indice k

    Return : retourne la kième liste
    """
    return l[k]
print(get_list_k(read_data(FILENAME),8))

def get_first(l):
    """"retourne le premier élément de cette liste 
    Arg : prend en argument une liste"""
    return l[0]
print(get_first(get_list_k(read_data(FILENAME),8)))

def get_last(l):
    """ donne le dernier élément de la liste
    arg : liste l
    """
    n = len(l)
    return l[n-1]
print(get_last(get_list_k(read_data(FILENAME),8)))


def get_max(l):
    """ donne le max de la liste
    arg : liste l
    """
    return max(l)
print(get_max(get_list_k(read_data(FILENAME),8)))

def get_min(l):
    """ donne le min de la liste
    arg : liste l
    """
    return min(l)
print(get_min(get_list_k(read_data(FILENAME),8)))

def get_sum(l):
    """ donne la somme des élément de la liste 
    arg : liste l
    """
    return sum(l)
print(get_sum(get_list_k(read_data(FILENAME),8)))


#### Fonction principale


def main():
    """faire appel aux fonctions secondaires pour vérifier leur bon fonctionnement."""
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
