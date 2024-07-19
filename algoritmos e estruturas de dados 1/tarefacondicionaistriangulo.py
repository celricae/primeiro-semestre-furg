ladoa = int(input("Digite o lado A: "))
ladob = int(input("Digite o lado B: "))
ladoc = int(input("Digite o lado C: "))

somaladoab = (ladoa + ladob)
somaladoac = (ladoa + ladoc)
somaladobc = (ladob + ladoc)

print(ladoa , ladob , ladoc)


if somaladoab >= ladoc and somaladoac >= ladob and somaladobc >= ladoa:

	print("O triângulo é válido!")
else:
	print("O triângulo não é válido")

if ladoa == ladob and ladoa == ladoc and ladob == ladoc:
	print("O triângulo é equilátero!")
else:
	if ladoa != ladob and ladoa != ladoc and ladob != ladoc:
	
