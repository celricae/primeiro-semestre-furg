numero = int(input("Digite um número inteiro: "))
divisor = 1
divisores = ""

while divisor <= numero:
    if numero % divisor == 0:
        divisores = divisores + str(divisor) + " "
    divisor = divisor + 1
print("os divisores são:", divisores)