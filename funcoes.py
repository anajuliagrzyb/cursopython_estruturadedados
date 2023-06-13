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
