'''
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____
'''
sequencia_a = [1, 3, 5, 7]
proximo_a = sequencia_a[-1] +2
print(proximo_a)

sequencia_b = [2, 4, 8, 16, 32, 64]
proximo_b = sequencia_b[-1] *2
print(proximo_b)

sequencia_c = [0, 1, 4, 9, 16, 25, 36]
proximo_c = (len(sequencia_c))**2
print(proximo_c)

sequencia_d = [4, 16, 36, 64,]
proximo_d = (len(sequencia_d) * 2 + 2) ** 2  
print(proximo_d)

sequencia_e = [1, 1, 2, 3, 5, 8]
proximo_e = sequencia_e[-1] + sequencia_e[-2]
print(proximo_e)

sequencia_f = [2, 10, 12, 16, 17, 18, 19]
proximo_f = sequencia_f[-1] + 1
print(proximo_f)