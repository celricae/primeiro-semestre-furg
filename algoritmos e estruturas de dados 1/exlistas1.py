'''
#1)Leia um String e escreva letra por letra.
nome = input("Escreva uma palavra: ")
cont = 0
while cont <= len(nome):
	print(nome[cont])
	cont+=1

#2)Leia um nome, escreva apenas as vogais e diga quantas vogais tem.
x = input("Escreva uma palavra: ")
cont = 0
vogal = ''
vogaltot = 0
while cont < len(x):
	if x[cont] == 'a' or x[cont] == 'e' or x[cont] == 'i' or x[cont] == 'o' or x[cont] == 'u':
		vogal = vogal + x[cont]
		vogaltot += 1
	cont += 1
print(f"As vogais são: {vogal} \nE o numero de vogais é : {vogaltot}")

#3)Leia uma palavra e mostre seu espelho.
nome = input("Escreva uma palavra: ")
invertido = ''
cont = 0
cont1 = -1
while cont < len(nome):
	invertido += nome[cont1]
	cont +=1
	cont1 -=1
print(invertido)

#3.a)Leia uma musica e uma vogal alvo. Escreva a musica trocando todas as vogais pela vogal algo.
sapo = input("Escreva uma frase: ")
vogalalvo = input("Escreva a vogal alvo: ")
cont = 0
sepe = ''
while cont < len(sapo):
	if sapo[cont] == 'A' or sapo[cont] == 'E' or sapo[cont] == 'I' or sapo[cont] == 'O' or sapo[cont] == 'U':
		sepe += vogalalvo
	else:
		sepe += sapo[cont]		
	cont += 1
print(sepe)
'''
#3.b)Leia um nome e faça o espelho do NOME, mantendo a "posição" de cada palavra.
nome = input("Escreva um nome: ")
emon = ''
cont = 0
cont1 = -1
while cont < len(nome):
	



