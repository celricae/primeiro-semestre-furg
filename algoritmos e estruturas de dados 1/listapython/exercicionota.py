not1=float(input("Insira a 1º nota: "))
not2=float(input("Insira a 2º nota: "))
not3=float(input("Insira a 3º nota: "))
not4=float(input("Insira a 4º nota: "))
freq=float(input("Insira a frequência em porcentagem: "))
if freq < 75:
	print("Esta rodado.")
else:
	if (not1+not2+not3+not4)/4 >= 7:
		print("Parabéns! Passou por média.")
	else:
		print("Está em exame.")
