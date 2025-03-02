n1 = float(input("Digite seu salario para reajuste: R$"))
n2 = (n1 * 0.15) + n1
print("Seu salario foi reajustado para: R${:2}".format(abs(n2)))
