# Python 3
import os
import argparse
from stat import S_ISDIR, S_ISREG


def walktree(top):
    '''parcourt récursivement le dossier et renvoit
    une liste avec tous les fichiers normaux'''
    liste = []
    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode  # give a code that
        # says whether it's a directory or a file
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            result = walktree(pathname)
            for _ in result:
                liste.append(_)
        elif S_ISREG(mode):
            liste.append(pathname.split('/')[-1])
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)
    return liste


def test_list(liste1, liste2):
    return [elem for elem in liste1 if elem not in liste2]


def affiche_liste(liste):
    liste = sorted(liste)
    print("-"*20)
    for i in liste:
        print(i)
    print("-"*20)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dossier1", help="chemin complet du premier dossier")
    parser.add_argument("dossier2", help="chemin complet du second dossier")
    args = parser.parse_args()
    chemin1 = args.dossier1
    chemin2 = args.dossier2

    liste_dossier1 = walktree(chemin1)
    liste_dossier2 = walktree(chemin2)

    print("\n")
    print("Fichiers présents dans " + chemin1 + " et absents dans " + chemin2)
    affiche_liste(test_list(liste_dossier1, liste_dossier2))
    print("\n")

    print("Fichiers présents dans " + chemin2 + " et absents dans " + chemin1)
    affiche_liste(test_list(liste_dossier2, liste_dossier1))
    print("\n")


if __name__ == '__main__':
    main()
