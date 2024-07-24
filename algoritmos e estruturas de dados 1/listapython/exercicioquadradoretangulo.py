larg=float(input("Insira a largura: "))
comp=float(input("Insira o comprimento: "))
if larg <= 0 or comp <=0:
	print("Valor inválido")
else:
	if larg == comp:
		print("É um quadrado")
	else:
		print("É um retângulo")
