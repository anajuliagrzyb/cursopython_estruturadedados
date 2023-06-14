l1 = ['carro', 'casa', 'apartamento']
l2 = ['geladeira', 'televisão']

l3 = l1 + l2
print(l3)

l2_2 = l2 * 2
print(l2_2)

print(l1[0])
print(l1[0:2])

l1.append('moto')
print(l1)

l1.remove('casa')
print(l1)

del(l1)
#print(l1)

for item in l2_2:
    print(item)

print("*******************************")

print("EXERCICIO LISTA")
soma = 0
lista = []
for i in range(1, 6):
    num = int(input("Digite um número: "))
    lista.append(num)
    print(lista)

for i in range(len(lista)):
    soma += lista[i]
    print(soma)


