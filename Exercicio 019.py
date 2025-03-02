import math
n1 = float(input("Digite o angulo: "))

se = math.sin(math.radians(n1))
co = math.cos(math.radians(n1))
ta = math.tan(math.radians(n1))

print("O seno é {:.2f}".format(se))
print("O cosseno é {:.2f}".format(co))
print("E a tangente é {:.2f}".format(ta))
