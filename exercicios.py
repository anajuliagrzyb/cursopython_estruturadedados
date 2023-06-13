# print("SOMA EM FOR")
# soma = 0
# for i in range(1, 6):
# num = int(input("Digite sua nota: "))
# soma = soma + num
# media = soma/5
# print(media)

# print("TABUADA EM FOR")
# tab = int(input("Digite a tabuada que deseja: "))
# for i in range(1, 11):
# tabuada = tab * i
# print(f"{tab} X {i} = {tabuada} ")
# print("*******************************")

# print("SOMA EM WHILE")
# soma = 0
# i = 1
# while i < 6:
# notas = int(input("Digite sua nota: "))
# i += 1
# soma = soma + notas
# media = soma/5
# print(media)

# print("TABUADA EM WHILE")
# i = 0
# tab = int(input("Digite a tabuada que deseja: "))
# while i < 10:
# i += 1
# tabuada = i * tab
# print(f"{tab} X {i} = {tabuada} ")
# print("*******************************")


# print("EXERCICIO LISTA")
# soma = 0
# lista = []
# for i in range(1, 6):
# num = int(input("Digite um número: "))
# lista.append(num)
# print(lista)

# for i in range(len(lista)):
# soma += lista[i]
# print(soma)
# print("*******************************")

# print("EXERCICIO DICIONÁRIO")
# alunos = {}
# soma = 0
# for _ in range(1, 4):
# nome = input('Digite o nome: ')
# nota = float(input('Digite a nota: '))
# alunos[nome] = nota
# alunos.values()
# print(alunos)

# for nota in alunos.values():
# soma += nota
# print('Média: ', soma/3)
# print("*******************************")

# print("EXERCICIO MATRIZ")
# soma = 0
# import numpy as np
# matriz = np.array([[3, 4, 1],
# [3, 1, 5]])
# matriz.shape
# for i in range(matriz.shape[0]):
# for j in range(matriz.shape[1]):
# soma += matriz[i][j]
# print(soma)

# def ler():
# temperatura = float(input('Digite a temperatura em graus Celsius: '))
# return temperatura

# def conversao(c):
# f = (9 * c + 160) / 5
# return f

# def mostrar(f):
# print(f)

# c = ler()
# f = conversao(c)
# mostrar(f)

#def ler():
    #velocidade = float(input('Digite a velocidade média: '))
    #tempo = float(input('Digite o tempo gasto: '))
    #return tempo, velocidade

#def calculo_distancia(tempo, velocidade):
    #return tempo * velocidade

#def calculo_litros(distancia):
    #return distancia / 12


#def resultado(tempo, velocidade, distancia, litros_usados):
    #print('Velocidade: ', velocidade)
    #print('Tempo: ', tempo)
    #print('Distância: ', distancia)
    #print('Litros: ', litros)

#tempo, velocidade = ler()
#distancia = calculo_distancia(tempo, velocidade)
#litros = calculo_litros(distancia)
#resultado(velocidade, tempo, distancia, litros)

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






