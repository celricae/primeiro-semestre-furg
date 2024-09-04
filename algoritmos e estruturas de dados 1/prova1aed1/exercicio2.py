dias = int(input("digite o número de dias: "))

dia = 1
mes = 1
ano = 2024
cd = 0
cm = 1
ca = 2024
while dias > 0:
	cd += 1
	dias -= 1
	dia = cd
	if dias >= 28 and mes == 2:
		cm += 1
		mes = cm
		cd -= 28
		dia = cd
	if dia >= 31 and (mes == 1 or mes == 3 or 5 == mes or mes == 7 or mes == 10):
		cm += 1
		mes = cm
		cd -= 31
		dia = cd
	if dia >= 30 and (mes == 4 or mes == 6 or mes == 8 or mes == 9 or mes == 11):
		cm += 1
		mes = cm
		cd -= 30
		dia = cd
	if mes == 12 and dia > 31:
		ca += 1
		ano = ca
		cd -= 31
		dia= cd
		cm -= 11
		mes = cm
data = (f"{dia}/{mes}/{ano}")
print(data)


