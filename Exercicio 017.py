n1 = float(input("Digite o valor do cateto oposto: "))
n2 = float(input("Digite o valor do cateto adjacente: "))
n3 = (n1 ** 2 + n2 ** 2) ** (1/2)
print("A hipotenusa é {:.2f}".format(n3))
