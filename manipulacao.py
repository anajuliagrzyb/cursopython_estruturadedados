'''
with open('/Users/ana.grzyb/Documents/cursopython_estruturadedados'
          '/frases.txt') as tex:
    for linha in tex:
        print(linha)
'''

'''
with open('/Users/ana.grzyb/Documents/cursopython_estruturadedados'
          '/frases.txt') as tex:
    r = tex.readlines()
    print(r)
'''

with open('texto2.txt', 'w') as texto:
    texto.write('Ola a todos')

with open('/Users/ana.grzyb/Documents/cursopython_estruturadedados'
          '/texto2.txt') as tex:
    for linha in tex:
        print(linha)
