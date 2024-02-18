contador = 0

resposta = input("Você telefonou para a vítima? \n")
if resposta == "Sim":
    contador += 1

resposta = input("Você esteve no local do crime? \n")
if resposta == "Sim":
    contador += 1

resposta = input("Você mora perto da vítima? \n")
if resposta == "Sim":
    contador += 1

resposta = input("Você devia para a vítima? \n")
if resposta == "Sim":
    contador += 1

resposta = input("Você já trabalhou para a vítima? \n")
if resposta == "Sim":
    contador += 1

if contador == 5:
    print("Assassino.")
elif contador >= 3:
    print("Cúmplice.")
elif contador == 2:
    print("Suspeito.")
else:
    print("Inocente.")