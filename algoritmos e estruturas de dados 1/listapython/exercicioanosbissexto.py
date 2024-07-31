#leia uma data DD,MM,AAAA e diga se ela é válida
#considere ano bissexto
dia=int(input("Informe o dia: "))
mes=int(input("Informe o mês: "))
ano=int(input("Informe o ano: "))
bissexto=0
if ano%100!=0 and (ano%4==0 or ano%400==0):
	bissexto="e o ano é bissexto"
else:
	bissexto="e o ano não é bissexto"
if dia > 31 or dia <= 0 or mes < 1 or mes >12:
	print("Data inválida")
else:
	if mes == 2 and dia > 28:
		print("Data inválida")
	else:
		if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
			print("Data inválida")
		else:
			print ("Data válida" , bissexto)
