tijolo = input("Insira o tijolo: ")
altura= int(input("Digite a altura: "))
cont = 1
andar = 1

espaco = "x"
desloc = altura - 1

while andar <= altura:
  cont2=0
  espaco_montado = ""
  while cont2 < desloc:
  	espaco_montado = espaco_montado + espaco
  	cont2 = cont2 + 1
  	
  cont2=0
  tijolo_montado = ""
  while cont2 < cont:
  	tijolo_montado = tijolo_montado + tijolo
  	cont2 = cont2 + 1
  print(espaco_montado + tijolo_montado)
  
  andar = andar + 1
  cont = cont + 2
  desloc = desloc - 1
