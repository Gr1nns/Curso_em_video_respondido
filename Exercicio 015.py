n1 = int(input("Digite os KM rodados: "))
n2 = int(input("Digite a quantidade de dias que você alugou o carro?: "))

n3 = n1 * 0.15
n4 = n2 * 60
n5 = n3 + n4

print("Você tera que pagar um total de R${:.2f}".format(n5))

