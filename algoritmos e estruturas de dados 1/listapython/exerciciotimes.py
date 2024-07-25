t1=input("Informe o primeiro time: ")
t2=input("Informe o segundo time: ")
t3=input("Informe o terceiro time: ")
t4=input("Informe o quarto time: ")

tf1="b"
tf2="a"

golt1xt2=float(input(f"Informe os gols do {t1} contra o {t2}: "))
golt2xt1=float(input(f"informe os gols do {t2} contra o {t1}: "))
golt3xt4=float(input(f"Informe os gols do {t3} contra o {t4}: "))
golt4xt3=float(input(f"informe os gols do {t4} contra o {t3}: "))

if golt1xt2 == golt2xt1:
    tf1=input(f"Informe qual time venceu a partida {t1} contra {t2}: ")
else:
    if golt1xt2 > golt2xt1:
        tf1 = t1
    else:
        if golt2xt1 > golt1xt2:
            tf1 = t2
if golt3xt4 == golt4xt3:
    tf2=input(f"Informe qual time venceu a partida {t3} contra {t4}: ")
else:
    if golt3xt4 > golt4xt3:
        tf2 = t3
    else:
        if golt4xt3 > golt3xt4:
            tf2 = t4
goltf1xtf2 = float(input(f"Informe os gols do {tf1} contra o {tf2}: "))
goltf2xtf1 = float(input(f"Informe os gols do {tf2} contra o {tf1}: "))

if goltf1xtf2 == goltf2xtf1:
    vencedor=input(f"Informe qual time venceu a partida final entre {tf1} e {tf2}: ")
    print(f"O vencedor da partida final é: {vencedor}")
else:
    if goltf1xtf2 > goltf2xtf1:
        vencedor = tf1
        print(f"O vencedor da partida final é: {vencedor}")
    else:
        vencedor = tf2
        print(f"O vencedor da partida final é: {vencedor}")
