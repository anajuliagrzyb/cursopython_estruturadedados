#forma crescente
for num in range (1, 6):
   print(num)
print("*******************************")

#forma decrescente
for num in range (5, 0, -1):
    print(num)
print("*******************************")

#soma
soma = 0
for num in range(1, 6):
    soma = soma + num
print(soma)
print("*******************************")


#for com string
palavra = 'sorvete'
for letra in palavra:
    print(letra)
    if letra == 'v':
        print("achou a letra V")
print("*******************************")

for i in range(0, 5):
    print(i)
    print('---')
    for j in range(0, 3):
        print(j)
    print()