dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano (2024 ou 2025): "))

if ano != 2024 and ano != 2025:
    print("só funciona com 2024 e 2025... reclama com o prisco.")
else:
    if ano == 2024:
        diasjaneiro = 31
        diasfevereiro = 29
        diasmarco = 31
        diasabril = 30
        diasmaio = 31
        diasjunho = 30
        diasjulho = 31
        diasagosto = 31
        diassetembro = 30
        diasoutubro = 31
        diasnovembro = 30
        diasdezembro = 31
    else:
        diasjaneiro = 31
        diasfevereiro = 28
        diasmarco = 31
        diasabril = 30
        diasmaio = 31
        diasjunho = 30
        diasjulho = 31
        diasagosto = 31
        diassetembro = 30
        diasoutubro = 31
        diasnovembro = 30
        diasdezembro = 31

    if mes < 1 or mes > 12:
        print("Mês inválido.")
    else:
        totaldias = 0

        if mes > 1:
            totaldias += diasjaneiro
        if mes > 2:
            totaldias += diasfevereiro
        if mes > 3:
            totaldias += diasmarco
        if mes > 4:
            totaldias += diasabril
        if mes > 5:
            totaldias += diasmaio
        if mes > 6:
            totaldias += diasjunho
        if mes > 7:
            totaldias += diasjulho
        if mes > 8:
            totaldias += diasagosto
        if mes > 9:
            totaldias += diassetembro
        if mes > 10:
            totaldias += diasoutubro
        if mes > 11:
            totaldias += diasnovembro
        
        totaldias += dia - 1

        if ano == 2024:
            diainicio = 1
        else:
            diainicio = 3

        diasemana = (totaldias + diainicio - 1) % 7

        nomedia = ""
        if diasemana == 0:
            nomedia = "segunda-feira"
        if diasemana == 1:
            nomedia = "terça-feira"
        if diasemana == 2:
            nomedia = "quarta-feira"
        if diasemana == 3:
            nomedia = "quinta-feira"
        if diasemana == 4:
            nomedia = "sexta-feira"
        if diasemana == 5:
            nomedia = "sábado"
        if diasemana == 6:
            nomedia = "domingo"

        print(f"A data {dia:02d}/{mes:02d}/{ano} cai em uma {nomedia}.")
