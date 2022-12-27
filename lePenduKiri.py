import random

############## Il faut fermer le fichier dès que tu en as plus besoin
fic = open("input.txt", "r")
contenu = fic.read()

liste = contenu.split() #tranforme le contenu en liste de mot mais la fonction split permet de transformer une chaine en liste
############## Pas nécessaire
for x in range (0,len(liste)):
	liste[x] = list(liste[x].strip()) #transforme chaque mot en liste de caractere

pv = int(input("Combien de vie voulez vous ?\n"))
score = 0
highscore = len(liste)
choix=None

############## Tu peux améliorer la condition
while ((pv >= 0) and (score != highscore) and (liste != [])) :  ############## Pas d'espace entre le while() et le :
	indice = random.randrange(0, len(liste), 1)
	while 0 != 1 :
		try:
			mot = liste[indice]
		except:
			indice = random.randrange(0, len(liste), 1)
		else:
			break

	saveMot = mot[:]
	mot2=mot[:]
	cache = "-"*len(mot)
	mot2="".join(mot2) ############## Pas compris pourquoi tu fais ça.. (cf. deuxième commentaire)

	while (pv >=0 and cache != mot2): ############## Absence d'espace après le >=


		print("\n\nVie : {}                       Score: {}\n".format(pv, score))
		print(cache, "\n")
		lettre= input(">>>>")

		cache = list(cache.strip())
		compteur=0					############## Absence d'espace 
		for x in range(0, len(mot)):
			if cache[x]==lettre:	############## Absence d'espace 
				print("Vous avez deja entre cette lettre")
			if mot[x] == lettre:
				cache[x]=mot[x]		############## Absence d'espace 
				compteur+=1		 	############## Absence d'espace 
		if compteur==0 :			############## Absence d'espace + Pas d'espace entre la fin du if et le :
			pv-=1					############## Absence d'espace 
		cache="".join(cache) #transforme la liste en chaine de caractere				 ############## Pas compris pourquoi tu fais ça.. (cf. deuxième commentaire)
			
	if pv < 0:
		print("Perdu !\nMerci d'avoir jouer")
	else:
		if liste==[]:				############## Absence d'espace 
			print("Fin de la partie (il n'y a plus de mot a deviner)")
		else:
			liste.remove(saveMot)
			score+=1				############## Absence d'espace 
			print("Mot suivant !\nVie:{}    et     Score:{}".format(pv, score))
	
############## https://www.python.org/dev/peps/pep-0008 ###################################
############## https://pypi.org/project/pep8/ ################################### ==> L'utilisation de ce package ne doit renvoyer aucune erreur