n1 = float(input("Digite a altura da parede: "))
n2 = float(input("Digite a largura da parede: "))
a = n1 * n2
p = n1 + n1 + n2 + n2
lt = a / 2
print("A area da parede é igual a {:2}, com um perimetro igual a {}".format(a, p))
print("A quantidade de tinta em litros que vc ira gastar para pintar a parede é {:0} Litros".format(lt))
