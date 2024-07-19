nome = input("Digite seu nome: ")
hora = int(input("Digite a hora: "))

if hora >=5 and hora <=11:
	print ("Bom dia, " , nome)
else: 
	if hora >11 and hora <18:
		print ("Boa tarde, " , nome)
	else:
		print("Boa noite, " , nome)
'''
nome = input("Digite seu nome: ")
hora = int(input("Digite a hora do dia: "))

if hora > 12:
	if hora > 18:
		saudacao = "Boa noite"
	else:
		saudacao = "Boa tarde"
else:
	if hora > 5:
		saudacao = "Bom dia"
	else:
		saudacao = "Boa noite"

print(f"{saudacao}, {nome}")	
'''
