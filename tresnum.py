num1 = int(input("Digite o 1 número: \n"))
num2 = int(input("Digite o 2 número: \n"))
num3 = int(input("Digite o 3 número: \n"))

if num1 > num2 and num1 > num3:
    print("O primeiro número é o maior.")
elif num2 > num1 and num2 > num3:
    print("O segundo número é o maior.")
else:
    print("O terceiro número é o maior.")