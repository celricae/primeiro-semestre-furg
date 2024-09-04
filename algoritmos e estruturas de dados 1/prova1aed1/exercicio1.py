lado1 = int(input("Escreva o lado 1 (número inteiro e positivo): "))
lado2 = int(input("Escreva o lado 2 (número inteiro e positivo): "))
area = lado1*lado2
if lado1 > 0 and lado2> 0:
	print("A área é: ", area)
else:
	print("Digite números inteiros e positivos!")
