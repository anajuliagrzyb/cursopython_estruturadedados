coleta = {'casa': 24, 'apartamento': 30, 'carro': 13}
print(coleta['casa'])

coleta['moto'] = 11
print(coleta)

del(coleta)['apartamento']
print(coleta)

print(coleta.items())
print(coleta.keys())
print(coleta.values())

coleta2 = {'televisao': 7, 'celular': 20}
print(coleta2)

coleta.update(coleta2)
print(coleta)

print(coleta.items())

for nome, quantidade in coleta.items():
    print(f'nome: {nome}, quantidade de produtos: {quantidade}')
