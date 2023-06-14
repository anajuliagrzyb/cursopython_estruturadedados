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

print('\n')
print("*******************************")
print("EXERCICIO DICIONÁRIO")
alunos = {}
soma = 0
nome = input('Digite o nome: ')

for _ in range(1, 4):
    nota = float(input('Digite a nota: '))
    alunos[nome] = nota
    alunos.values()
    print(alunos)

for nota in alunos.values():
    soma += nota
    print('Média: ', soma/3)