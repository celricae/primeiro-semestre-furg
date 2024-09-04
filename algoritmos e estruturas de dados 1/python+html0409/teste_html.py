print("<h1>Tábuada</h1><hr>")

numero = 0
mult = 0
cont = 0
print('<table border=1>')

while cont < 11:
	print("<tr>")
	print(f"<td>{cont}X{mult}</td>")
	print(f"<td>{cont*mult}</td>")
	print("</tr>")
	mult = mult + 1
	if mult == 11:
		mult = 0
		cont += 1
	
print('</table>')
