sen=input("Digite a senha: ")

cont=4


while sen != "buddy holly" and cont >=1: 
	print("Senha incorreta!\ntentativa restantas:," , cont)
	sen=input("Digite a senha novamente: ")
	cont = cont-1
if cont == 0:
	print("Muitas tentativas! e o marcos não sabe cortar frango")
if sen == "buddy holly":
	print("Senha correta! e o marcos não sabe cortar frango")
