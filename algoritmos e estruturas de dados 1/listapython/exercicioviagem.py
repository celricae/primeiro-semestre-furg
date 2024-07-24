preco=input("A viagem custará menos que R$30? ")
wifi=input("Terá Wifi? ")
pisc=input("Terá piscina? ")
chu=input("Terá churrasqueira? ")
if preco=="não":
	print("Não ocorrerá viagem.")
else:
	if pisc=="sim" and wifi=="sim":
		print("Ocorrerá viagem.")
	else:
		if (pisc=="não" or wifi=="não") and chu=="sim":
			print ("Ocorrerá viagem.")
		else:
			print("Não ocorrerá viagem.")
