num=int(input("Digite um número inteiro e positivo: "))
if num > 1:
    if num%num==0 and num%1==0:
        print("O número", num, "é primo.")
    else:
        print("O número", num, "não é primo.")