'''
class Triangulo:
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura / 2)

    def tipo(self):
        if self.lado1 > self.lado2 + self.lado3:
            return 'NÃO é triângulo'
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado1 == self.lado2:
            return 'triângulo isóceles'
        else:
            return 'outro tipo de triângulo'


t1 = Triangulo(2, 1, 3, 4, 3)
print(t1.lado1, t1.lado2, t1.lado3, t1.base, t1.altura)
print(t1.area())
print(t1.tipo())
print('\n')
t2 = Triangulo(8, 8, 8, 16, 9)
print(t2.lado1, t2.lado2, t2.lado3, t2.base, t2.altura)
print(t2.area())
print(t2.tipo())

'''
import self as self

print('EXERCICIO')

class Aluno:
    def __init__(self, aluno, nota1, nota2):
        self.aluno = aluno
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0

    def calculo(self):
        self.media =  (self.nota1 + self.nota2)/ 2
        return self.media

    def mostra(self):
        print('Nome: ', self.aluno)
        print('Nota 1: ', self.nota1)
        print('Nota 2: ', self.nota2)
        print('Média: ', self.media)

    def aprovados(self):
        if self.media >= 6.0:
            print('APROVADO')
        else:
            print('REPROVADO')


a1 = Aluno('Ana Julia', 10.0, 10.0)
print(a1.mostra())
print(a1.aprovados())
media = a1.calculo()
print(media)
print('\n')
a2 = Aluno('Guilherme', 5.0, 3.0)
print(a2.mostra())
print(a2.aprovados())
media = a2.calculo()
print(media)




