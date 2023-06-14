#funções sem parâmetro e sem retorno
#def mensagem():
    #print('Texto da função')
#print(mensagem())

#funções com passagem de parâmetro
#def mensagem(texto):
    #print(texto)
#print(mensagem('texto 1'))
#print(mensagem('texto 2'))
#print(mensagem('texto 3'))

#def soma(a, b):
    #print (a + b)
#print(soma(2, 3))


#Funções com passagem de parâmetros e retorno
def soma(a, b):
    return a + b
print(soma(3, 2))

r = soma(3, 2)
print(r)

def calculo_energia_potencial_gravitacional(m, h, g=10):
    '''
    Calcula a energia potencial gravitacional
    m: massa como uma variável float
    h: altura como uma variável float
    g: aceleração gravitacional, com valor default de 10

    '''
    e = g * m * h
    return e
print(calculo_energia_potencial_gravitacional(30, 12))
print(calculo_energia_potencial_gravitacional(30, 12, 9.8))

print('\n')
print("*******************************")
print('\n')


print('EXERCICIO 1')
def ler():
    temperatura = float(input('Digite a temperatura em graus Celsius: '))
    return temperatura

def conversao(c):
    f = (9 * c + 160) / 5
    return f

def mostrar(f):
    print(f)

c = ler()
f = conversao(c)
mostrar(f)

print('\n')
print('EXERCICIO 2')

def ler():
    velocidade = float(input('Digite a velocidade média: '))
    tempo = float(input('Digite o tempo gasto: '))
    return tempo, velocidade

def calculo_distancia(tempo, velocidade):
    return tempo * velocidade

def calculo_litros(distancia):
    return distancia / 12


def resultado(tempo, velocidade, distancia, litros_usados):
    print('Velocidade: ', velocidade)
    print('Tempo: ', tempo)
    print('Distância: ', distancia)
    print('Litros: ', litros)

velocidade, tempo = ler()
distancia = calculo_distancia(tempo, velocidade)
litros = calculo_litros(distancia)
resultado(velocidade, tempo, distancia, litros)

