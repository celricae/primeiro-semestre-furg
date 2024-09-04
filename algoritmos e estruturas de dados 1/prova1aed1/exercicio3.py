num = int(input("Escreva um número inteiro e positivo entre 1000 e 9999: "))
n = 0
u = 0
m = 0
e = 0
mun = 0
if num < 1000 or num > 9999:
	print("Número inválido!")
else:
	if num > 1000 and num <= 9999:
			n = num//1000
			u = ((num%1000)-(num%100))//100
			m = ((num%100)-(num%10))//10
			e = num%10
			num=(f"{e}{m}{u}{n}")
			print(num)
