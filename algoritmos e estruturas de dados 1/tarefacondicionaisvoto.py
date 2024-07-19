nascimento = int(input("Digite o ano em que você nasceu: "))
ano = 2024
idade = ano-nascimento
print(idade)


if idade < 16:
	print("Não pode votar!")
else:
	if idade >= 16 and idade < 18 or idade >= 70:
		print("O voto é facultativo!")
	else:
		if idade >= 18 and idade < 70:
			print("O voto é obrigatório!")
