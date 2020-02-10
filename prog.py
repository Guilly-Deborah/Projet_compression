# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:21:04 2020

@author: guillyd
"""

class Texte:
    
    def __init__(self,contenu):
        '''
        Definit le contenue du texte
        '''
        self.contenu=contenu
    
    def frequences(self):
        '''
        Donne la liste des caracteres et leur frequences 
        trie par ordre croissant des frequences et des caracteres
        ex: [['a',1]['c',1]['b',2]]
        '''
        #Initialisation des listes
        self.alphabet=[]
        freq=[]
        #Pour chaque element du contenu
        for i in self.contenu:
            #Si le caractere n'est pas deja dans alphabet
            if i not in self.alphabet:
                #ajout aux listes frequence et alphabet
                freq+=[[i,1]]
                self.alphabet+=[i]
            else:
                #Sinon on recherche le caractere dans frequence et on ajoute 1 a sa frequence
                for f in freq:
                    if i==f[0]:
                        f[1]=f[1]+1
        return(self.tribulle(freq))
                
    def tribulle(self,liste):
        '''
        Tri une liste donnee
        '''
        #Initialisation
        L=liste
        index=len(liste)
        for i in range(index):
            #Index avant l'index i 
            for j in range(0,index-i-1):
                #Si la frequence du j-eme element est plus grande que celle du j+1-eme element
                if L[j][1]>L[j+1][1]:
                    #Inversion des deux elements
                    L[j],L[j+1]=L[j+1],L[j]
                #Si pour la meme frequence, le code ASCII j-eme element est plus grand que celui du j+1-eme element
                elif L[j][1]==L[j+1][1] and L[j][0]>L[j+1][0]:
                    #Inversion des deux elements
                    L[j],L[j+1]=L[j+1],L[j]        
        return L
  
    def feuilles(self,freq):
        '''
        Cree la liste des arbres a partir d'une liste de frequence
        '''
        #Initialisation
        liste_feuilles=[]
        #Parcours de la liste des frequences
        for element in freq:
            #Creation du nouveau noeud
            n=Node(element[0],element[1])
            liste_feuilles+=[n]
        return liste_feuilles

class Node:
    
    def __init__(self,caractere,frequence,fil_gauche=None,fil_droit=None):
        '''
        Constructeur d'un noeud
        caractere = un caractere du texte 
        frequence = frequence associee a ce caractere
        fil_gauche = son fil gauche
        fil_droit= son fil droit
        '''
        self.caractere=caractere
        self.frequence=frequence
        self.fil_gauche=fil_gauche
        self.fil_droit=fil_droit
    
    def get_caractere(self):
        '''
        Retourne le caractere du noeud
        '''
        return self.caractere
    
    def get_frequence(self):
        '''
        Retourne la frequence du noeud
        '''
        return self.frequence
        
    def get_fils(self):
        '''
        Retourne la liste des fils d'un noeud
        '''
        return [self.fil_gauche,self.fil_droit]
    
    def get_fil_gauche(self):
        '''
        Retourne le fil gauche d'un noeud
        '''
        return self.fil_gauche
    
    def get_fil_droit(self):
        '''
        Retourne le fil droit d'un noeud
        '''
        return self.fil_droit
    
    def get_pere(self,liste_noeuds):
        '''
        Retourne le pere d'un noeud
        '''
        #Parcour de la liste des noeuds
        for noeud in liste_noeuds:
            #Si le noeud considere est le fil du noeud de la liste
            if self in noeud.get_fils():
                return noeud


class Tree:

    def tribulle(self,liste):
        '''
        Tri une liste donnee
        '''
        #Initialisation
        L=liste
        index=len(liste)
        for i in range(index):
            #Index avant l'index i 
            for j in range(0,index-i-1):
                #Si la frequence du j-eme noeud est plus grande que celle du j+1-eme noeud
                if L[j].get_frequence()>L[j+1].get_frequence():
                    #Inversion des deux elements
                    L[j],L[j+1]=L[j+1],L[j]       
        return L       

    def index_deux_mini(self,liste):
        '''
        Retourne les index des deux plus petit element d'un liste
        La frequence du premier element est inferieur ou egale a celle du second element
        '''
        #Initialisation des variables
        index_mini1=0
        index_mini2=1
        #Si a l'initialisation, les element sont inverser
        if liste[index_mini2].get_frequence()<liste[index_mini1].get_frequence():
            index_mini2,index_mini1=index_mini1,index_mini2
        #Parcour du reste de la liste
        for i in range(2,len(liste)):
            #Si la frequence de l'element i est plus petite que celle de l'element mini2
            if liste[i].get_frequence()<liste[index_mini2].get_frequence():
                #Si la frequence de l'element i est plus petite que celle de l'element mini1
                if liste[i].get_frequence()<liste[index_mini1].get_frequence():
                    index_mini1=i
                else:
                    index_mini2=i
        return (index_mini1,index_mini2)
    
    
    def rest(self,liste,retirer1,retirer2):
        '''
        Donne une liste sans les deux elements retirer1 et retirer2
        '''
        #Initialisation
        R=[]
        #Parcours de tous les elements de la liste
        for i in liste:
            #Si ce n'est pas un des elements a retirer
            if i!=retirer1 and i!=retirer2:
                R+=[i]
        return R
    
    def arbre(self,liste_feuilles):
        '''
        Creation de l'arbre de Huffman
        Retourne la liste contenant la racine et la liste de tous les noeuds
        '''
        #Initialisation des listes
        liste_racine=liste_feuilles
        liste_noeuds=liste_feuilles
        #Tant que l'on a pas de racine unique
        while len(liste_racine)!=1:
            #Tri de la liste des noeuds selon la frequence
            liste_trier=self.tribulle(liste_racine)
            #Recuperation de index des deux element avec les plus petites frequences
            (index_gauche,index_droit)=self.index_deux_mini(liste_trier)
            #Calcul de la nouvelle frequence
            new_freq=liste_trier[index_gauche].get_frequence()+liste_trier[index_droit].get_frequence()
            #Creation du nouveau noeud
            new_node=Node("",new_freq,liste_trier[index_gauche],liste_trier[index_droit])
            #Ajout de ce noeud aux listes
            liste_racine+=[new_node]
            liste_noeuds+=[new_node]
            #Retrait du noeud et de ses fils dans la liste des noeuds a traite 
            liste_racine=self.rest(liste_racine,liste_trier[index_gauche],liste_trier[index_droit])
        return (liste_racine,liste_noeuds)
    
    def chemin(self,element,liste_racine,liste_noeuds):
        '''
        Retourne le chemin depuis la racine vers le noeud avec le caractere voulu
        '''
        #Recuperation de la racine
        racine=liste_racine[0]
        #Parcour de tous les noeuds
        for i in liste_noeuds:
            #Si le noeud a le caractere cherche 
            if i.get_caractere()==element:
                noeud_voulu=i
        #Recherche du premier pere
        pere=noeud_voulu.get_pere(liste_noeuds)
        #Ajout du premier pere et du fil au chemin
        chemin=[pere,noeud_voulu]
        #Tant que le pere est different de la racine
        while pere!=racine:
            #Rechcher du pere precedent
            pere=pere.get_pere(liste_noeuds)
            #Ajout de ce pere au chemin
            chemin=[pere]+chemin
        return chemin
    
    def codage(self,element,chemin):
        '''
        Retourne le code binaire de l'element donne
        '''
        #Initialisation
        code =''
        i=0
        #Tant que l'elemnt du chemin est different de l'element donne
        while chemin[i].get_caractere()!=element :
            #Si l'element suivant est le fil gauche de l'element considere, on ajout 0 au code
            if chemin[i+1]==chemin[i].get_fil_gauche():
                code+='0'
            #Sinon on ajout 1 au code
            elif chemin[i+1]==chemin[i].get_fil_droit():
                code+='1'
            i+=1
        return code


if  __name__=='__main__':
    name=input("nom du fichier :")
    fichier=open(name+".txt","r")
    #Recuperation du contenu
    contenu=fichier.read()
    #Fermeture du fichier
    fichier.close()
    #Appliquation a la classe Texte
    text=Texte(contenu)
    #Creation de la liste des frequences associee au fichier
    Freq=text.frequences()
    #Initialisation de l'arbre
    tree=Tree()
    #Creation de la liste des feuilles
    liste_feuilles=text.feuilles(Freq)
    #Creation de l'arbre
    A=tree.arbre(liste_feuilles)
    #Initialisation du code binaire
    code=''
    #Parcours des elements et ajout du code de chaque element au code du texte
    for element in contenu:
        chemin=tree.chemin(element,A[0],A[1])
        code+=tree.codage(element,chemin)
    #Rajout de zero pour obtenir un resulat sous forme d'octets
    while len(code)%8!=0:
        code+='0'

    #Creation du fichier des frequences
    fichier_freq=open(name+"_freq.txt","w")
    #Ecriture de la taille de l'alphabet
    fichier_freq.write(str(len(text.alphabet))+"\n")
    #Ecriture de chaque caracteres avec leurs frequences
    for l in Freq:
        fichier_freq.write(str(l[0])+" "+str(l[1])+"\n")
    #Fermeture du fichier
    fichier_freq.close()

    code_b=code.encode()
    #Creation du fichier compresse
    fichier_bin=open(name+"_comp.bin","wb")
    #Ecriture du code dans le fichier
    for e in code:
        if e=='0':
            fichier_bin.write(b'0')
        else:
            fichier_bin.write(b'1')
    #Fermeture du fichier
    fichier_bin.close()
