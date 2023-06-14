

'''
import leitura as lt

texto = lt.ler_string('Digite seu nome: ')
print(texto)

numero = lt.ler_float('Digite o valor 1: ')
print(numero)
'''
'''

lista = []
try:
    lista.append(float(input('Digite o primeiro valor: ')))
    lista.append(float(input('Digite o segundo valor: ')))
    divisao = lista[0] / lista[1]
except ValueError:
    print('ERRO! Valor Inválido.')
except ZeroDivisionError:
    print('ERRO! Divisão por zero.')
except IndexError:
    print('ERRO! Indice invalido.')
except KeyboardInterrupt:
    print('Usuário interrompeu a execução.')
else:
    print(f'A divisão é {divisao}')


'''

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Ana': 7.5}
print(alunos)

with open('alunos.txt', 'w') as arquivo:
    for aluno, nota in alunos.items():
        arquivo.write(f'{aluno}, {nota}\n')

with open('alunos.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)






