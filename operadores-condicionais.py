if 5 > 3:
    print('5 é maior que 3')
#print('teste')

print('**************************')

if 5 > 4:
    print('5 é maior')
else:
    print('5 não é maior')

print('**************************')

n = 9
if n == 4:
    print('n é igual a 4')
else:
    if n == 3:
        print('n é igual a 3')
    else:
        print('n não é igual a 3 nem a 4')

print('**************************')

x = 1
y = 4
if(x > 1) or (y % 2 == 0):
    print('x é maior que 1 e y é par')
else:
    print('Uma ou nenhuma das condições foram satisfeitas')

print('**************************')

print('EXERCICIO 1')
idade = int(input('Digite a sua idade: '))

if (idade > 0) and (idade <= 12):
    print('Criança')
elif (idade > 13) and (idade <= 17):
    print('Adolescente')
elif (idade > 18):
    print('Adulto')
else:
    print('IDADE É INVALIDA')

print('\n')
print('EXERCICIO 2')

m1 = float(input('Digite a primeira nota: '))
m2 = float(input('Digite a segunda nota: '))
m3 = float(input('Digite a terceira nota: '))

media = (m1 + m2 + m3) / 3
print(media)
if (media > 4.1) and (media <= 6.0):
    print('EXAME')
elif media > 6:
    print('APROVADO')
else:
    print('REPROVADO')
