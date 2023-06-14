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
print("*******************************")
print('\n')
print('EXERCICIOS')


print("SOMA EM WHILE")
soma = 0
i = 1
while i < 6:
    notas = int(input("Digite sua nota: "))
    i += 1
    soma = soma + notas
    media = soma/5
    print(media)

print("TABUADA EM WHILE")
i = 0
tab = int(input("Digite a tabuada que deseja: "))
while i < 10:
    i += 1
    tabuada = i * tab
    print(f"{tab} X {i} = {tabuada} ")
