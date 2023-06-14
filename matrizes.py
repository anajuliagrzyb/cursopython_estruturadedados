import numpy as np

matriz = np.array([[2, 3, 1],
                   [4, 5, 7]])
print(matriz)
print(matriz.shape)
print(matriz[0])
print(matriz[0][0])

for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i][j])

print('\n')
print("*******************************")
print("EXERCICIO MATRIZ")
soma = 0
import numpy as np
matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])
matriz.shape
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        soma += matriz[i][j]
        print(soma)



