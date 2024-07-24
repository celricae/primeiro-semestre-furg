num1=float(input("Insira o primeiro número: "))
num2=float(input("Insira o segundo número: "))
num3=float(input("Insira o terceiro número: "))
if num3>num2 and num2>num1:
	print(num1 , num2 , num3)
if num2>num3 and num3>num1:
	print(num1 , num3 , num2)
if num1>num3 and num3>num2:
	print(num2 , num3 , num1)
if num3>num1 and num1>num2:
	print(num2 , num1 , num3)
if num2>num1 and num1>num3:
	print(num3 , num1 , num2)
if num1>num2 and num2>num3:
	print(num3 , num2 , num1)
