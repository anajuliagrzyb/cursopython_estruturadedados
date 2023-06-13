#crescente
num = 1
while num < 6:
    print(num)
    num += 1
print("*******************************")

#decrescente
num = 5
while num > 0:
    print(num)
    num -= 1
print("*******************************")

#soma
soma = 0
num = 1
while num < 6:
    soma += num
    num += 1
print (soma)
print("*******************************")

num = -1
while num < 1 or num > 10:
    num = int(input('Digite um número de 1 a 10: '))