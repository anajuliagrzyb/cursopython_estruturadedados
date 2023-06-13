produtos = ('celular', 'carregador', 'fone', 'case',
            'celular', 'carregador', 'celular')
print(produtos)

print(set(produtos))

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)
print(c3)

print(c1.difference(c2))
print(c2.difference(c1))

