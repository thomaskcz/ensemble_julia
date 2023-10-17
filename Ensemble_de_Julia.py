""" 
Module permettant de générer et d'afficher l'ensemble de Julia de paramètre c
Les images sont sauvegardées dans le dossier Images_Julia qui sera créé si il n'existe pas
"""

import os # Module pour les chemins de fichiers
import matplotlib.pyplot as plt # Module d'affichage
import numpy as np # Module pour les tableaux

def conv(z0,n,p,c):
    """ Teste si la suite complexe u_n=z_n converge vers l'infini ou non au bout de n itérations

    Args:
        z0 (complex): premier terme de la suite
        n (int): nombre d'itérations
        p (float): rayon de convergence
        c (complex): paramètre c

    Returns:
        bool: True si la suite converge vers l'infini, False sinon
    """
    z=z0
    i=0
    while i<n and abs(z)<p:
        z=z*z+c
        i+=1
    # Si i==n, alors on peut considérer que la suite converge
    return i==n

def save(l,h,rx,ry,n,p,c):
    """ Affiche l'ensemble de Julia de paramètre c dans le rectangle de largeur l et de hauteur h
        avec une résolution rx*ry et un nombre d'itérations n et un rayon de convergence p.

        Attention : l'axe des ordonnées est inversé par rapport à la convention mathématique
                    si la résolution n'est pas proportionnelle à la taille, l'image sera déformée

    Args:
        l (int): largeur du rectangle (dans le plan complexe)
        h (int): hauteur du rectangle (dans le plan complexe)
        rx (int): résolution en x
        ry (int): résolution en y
        n (int): nombre d'itérations
        p (float): rayon de convergence
        c (complex): paramètre c
    """

    X=np.linspace(-l/2,l/2,rx)
    Y=np.linspace(-h/2,h/2,ry)
    # On crée un tableau de taille rx*ry avec des zéros
    image=np.zeros([rx,ry])
    for i in range(rx):
        for j in range(ry):
            z=complex(Y[j],X[i])
            if conv(z,n,p,c):
                image[i][j]=1

    # On récupère le chemin du dossier contenant le fichier python
    path=__file__
    path=path.split("/")
    path="/".join(path[:-1])

    # On crée le dossier Images_Julia s'il n'existe pas
    path+="/Images_Julia"
    if not os.path.isdir(path):
        os.mkdir(path)

    # On sauvegarde l'image en noir et blanc
    plt.imsave(f"{path}/{str(c.real)}_{str(c.imag)}i.png",image,cmap='gray')


# Ce test permet de ne pas exécuter le code ci-dessous si on importe le module
if __name__=="__main__":
    # On génére quelques exemples
    save(3,4,750,1000,100,10**10,-1)
    save(3,3,1000,1000,100,10**10,0)
    save(3,3,1000,1000,100,10**10,0.285+0.013j)
    save(3,3,1000,1000,100,10**10,0.3+0.5j)
    save(3,3,1000,1000,100,10**10,-0.4+0.6j)
    save(3,4,750,1000,100,10**10,-0.8+0.156j)
