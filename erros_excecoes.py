'''
 TRATAMENTO DE ERROS E EXCEÇÕES

- NameError: variável não foi definida
- TypeError: tipos de dados incompatíveis
- RuntimeError: erro de execução
- SyntaxErro: sintaxe digitada é inválida e não reconhecida pelo interpretador
- ZeroDivisionError: divisão por zero
- IndexError: índice está fora da colecão
'''


#Tipos de erros
'''
3 = 4                        # --> SyntaxError, deveria ter sido colocado uma variavel no lugar do 3.
print('Meu nome é ', nome)   # --> NameError, a variável nome não foi definida.
print(3 / 0)                 # --> ZeroDvisionError, erro por estar tentando dividir um número por zero.
2.3 / 'cachorro'             # --> TypeError, dá esse erro pq um número não pode ser dividido por uma string.
c = [1,2,3,4,5]
c[5]                         # --> IndexError, esse erro se dá pq a posição pedida está fora da faixa

'''

#Tratamento de erros
'''
while True:
 try:
     n = int(input('Digite um número inteiro: '))
 except:
     print('Valor inválido')
 else:
     print(f'Valor digitado é {n}')
     break
'''

while True:
    try:
        p = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Valor inválido')
    except KeyboardInterrupt:
        print('Usuário interrompeu a execução')
    else:
        print(f'Valor digitado é {p}')
        break
