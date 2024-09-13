import random

random.seed()
sorte = [0,0,0,0,0,0,0,0,0,0,0]
cont = 0
porcentagem = []
while cont < 1000:
	valor = random.randint(0,10)
	sorte[valor] = sorte[valor] + 1
	print(sorte)
	cont = cont + 1
	
for item in sorte:
	porcentagem.append(100* item/cont)
print(porcentagem)
