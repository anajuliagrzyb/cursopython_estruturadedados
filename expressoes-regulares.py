'''

METACARACTERES
. - qualquer caractere(execeto linha nova)
\w - qualquer caracter alfanumerico
\W - qualquer caractere não-alfanumerico
\d - qualquer caractere que seja um digito(0-9)
\D - qualquer caractere não digito
\s - espaço em branco
^-  começa com
$- termina com
\ - usado antes de metacaracteres para especificar seu signicado literal

QUANTIFICADORES
Permitem determinar como e quantas vezes os metacaracteres aparecem
[] - opcional entre os que estão dentro dos colchetes
() - captura grupos de caracteres
* - de zero a mais vezes
? - zero ou mais vezes
+ - uma ou mais vezes
{m, n} - de M a N vezes
| - ou

'''

import re

#FUNÇÃO SEARCH
frase = 'Ola, meu numero de telefone é (42)0000-0000'
print(re.search('\(\d{2}\)\d{4,5}-\d{4}', frase))

frase = 'A placa de carro que eu anotei durante o acidente foi FRT-1998'
print(re.search('[A-Za-z]{3}-\d{4}', frase))

email = 'Entre em contato, meu email é teste@teste.com'
print(re.search('\w+@\w+\.com', email))

#FUNÇÃO MATCH
frase = 'A placa de carro que eu anotei durante a batida foi FRT-1998'
print(re.match('[A-Za-z]{3}-\d{4}', frase))

frase2 = 'FRT-1998 é a placa do carro'
print(re.match('[A-Za-z]{3}-\d{4}', frase2))


#FUNÇÃO FINDALL
frase3 = 'Meu número de telefone atual é (42)0000-0000. O número (56)1111-1111 é o antigo'
print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase3))

emails = '''
Nome: teste 1
email: teste1@teste.com
Nome: teste 2
email: teste2@teste.com
Nome: teste 3
email: teste3@teste.com
'''
print(re.findall('\w+@\w+\.com', emails))


print('EXERCICIO')

num = '''
Rua Alcion, 296
Av. Satelite, 908
Av. Amor, 1234
Av. Carlos, 8907
'''
print(re.findall('\d{3,4}', num))


cep = 'Os números dos CEPs são 08331-010, 00000-000, 12345-123'
print(re.findall('[0-9]{5}-[0-9]{3}', cep))

url = 'https://www.google.com'
print(re.findall('https?://[A-Za-z0-9./]+', url))
