precogas = 5.85
desempenho = float(input("Digite o desempenho do carro (km/l): "))
trajeto = float(input("Digite o trajeto percorrido no mês (km): "))
if desempenho <= 0 or trajeto <= 0:
    print("Valores inválidos")
else:
    consumo = trajeto / desempenho
    total = consumo * precogas
    print(f"O gasto total com combustível será de R${total:.2f}")
