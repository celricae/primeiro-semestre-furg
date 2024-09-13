import random

random.seed()
'''
while True:
	print(random.randint(0,10))
'''	
#1.a) Leia duas palavras e escreva se elas são anagramas.

#1.b) Leia um nome e escreva um anagrama aleatório desse nome.

#2.a) Gere uma senha forte aleatória. Pergunte ao usuário se quer que tenha número e/ou letras.
	#ex: Prisco ---> os45c*&riP

#1.a)
'''
pala1 = input("Digite a primeira palavra: ")
pala2 = input("Digite a segunda palavra: ")
contagem1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
contagem2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
pala1 = pala1.lower()
pala2 = pala2.lower()
if len(pala1) == len(pala2):
	for letra in pala1:
		indice = ord(letra) - ord('a')
		contagem1[indice] = contagem1[indice] + 1
	for letra in pala2:
		indice = ord(letra) - ord('a')
		contagem2[indice] = contagem2[indice] + 1
	
	anagrama = True
	cont = 0
	while anagrama and cont < len(contagem1):
		if contagem1[cont] != contagem2[cont]:
			anagrama = False
		cont = cont + 1
	if anagrama:
		print("É um anagrama!")
	else:
		print("Não é anagrama...")
else:
	print("As palavras tem tamanhos diferentes!")

#método alternativo:
pala1 = input("Digite a primeira palavra: ")
pala2 = input("Digite a segunda palavra: ")
contagem = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
pala1 = pala1.lower()
pala2 = pala2.lower()
if len(pala1) == len(pala2):
	for letra in pala1:
		indice = ord(letra) - ord('a')
		contagem[indice] = contagem[indice] + 1
	for letra in pala2:
		indice = ord(letra) - ord('a')
		contagem[indice] = contagem[indice] - 1
	if contagem == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
		print("É um anagrama!")
	else:
		print("Não é anagrama...")
else:
	print("As palavras tem tamanhos diferentes!")
'''
#metodo *MAIS* alternativo:

str1 = input("digite: ")
str2 = input("digite: ")
lista = []

if len(str1) == len(str2):
	print("Pode ser anagrama....")
	anagrama = True
	for letra in str1:
		lista.append(letra)
	print(lista)
	
	for letra in str2:
		indice = 0
		achei = False
		while indice < len(lista) and achei == False:
			if letra == lista[indice]:
				achei = True
				lista.pop(indice)
			indice = indice + 1
		if achei == False:
			anagrama = False
			print("Não é anagrama.")
	if anagrama:
		print("É anagrama.")
else:
	print("Não é anagrama....")
'''
#1.b)
nome = input("Digite um nome: ")
nome = nome.lower()

nome = 
'''
