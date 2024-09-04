'''
#aula listas
compras = ['nutella','pão','queijo','coquinha','patê','carne']
lucas = ['lucas',20,1.70,'RG',['arroz','feijão','nhoque']]
compras[4] = 'brigadeiro'
compras.append('nescau')
i = 0

while i < len(compras):
	print(compras[i])
	i = i+1
#linhas 5-13 = iterando uma lista

for produto in compras:
	print(produto)
	
#pesquisar programação orientada ao objeto
'''
#Pergunte ao usuário os produtos da compra e depois printe em formato de lista.

compras = []
preco = []
i = 0
prod = ' '
pre = ''
total = 0

while prod != '':
	prod = input("Digite o produto (ou não digite nada para finalizar o programa): ")
	pre = input("Digite o preço do ultimo produto (se não existir último produto não digite nada): ")
	if len(pre) > 0:
		pre = float(pre)
		compras.append(prod) #adiciona um item na lista, aumentando o tamanho dela.
		preco.append(pre)
		total += pre
print(compras,preco)

while i < len(compras):
	print(f'{compras[i]} custa R${preco[i]:.2f}')
	i = i+1
print(f'O total é: R${total:.2f}')	

print('------------------------------------------')

for prod in compras:
	print(prod)
