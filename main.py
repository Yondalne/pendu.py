import random

fic = open("input.txt", "r")
contenu = fic.read()

liste = contenu.split("\n") #tranforme le contenu en liste de mot mais la fonction split permet de transformer une chaine en liste 
print(liste)
for x in range (0,len(liste)):
	liste[x] = list(liste[x].strip()) #transforme chaque mot en liste de caractere

pv = int(input("Combien de vie voulez vous ?\n"))
score = 0
highscore = len(liste)
choix=None

while ((pv >= 0) and (score != highscore) and (liste != [])) :
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
	mot2="".join(mot2)

	while (pv >=0 and cache != mot2):
		print("\n\nVie : {}                       Score: {}\n".format(pv, score))
		print(cache, "\n")
		lettre= input(">>>>")

		cache = list(cache.strip())
		compteur=0
		for x in range(0, len(mot)):
			if cache[x]==lettre:
				print("Vous avez deja entre cette lettre")
			if mot[x] == lettre:
				cache[x]=mot[x]
				compteur+=1
		if compteur==0 :
			pv-=1
		cache="".join(cache) #transforme la liste en chaine de caractere
			
	if pv < 0:
		print("Perdu !\nMerci d'avoir jouer")
	else:
		if liste==[]:
			print("Fin de la partie (il n'y a plus de mot a deviner)")
		else:
			liste.remove(saveMot)
			score+=1
			print("Mot suivant !\nVie:{}    et     Score:{}".format(pv, score))