turno = input("Insira o turno que você estuda sendo M-Matutino, V-Vespertino e N-Noturno.\n")

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")