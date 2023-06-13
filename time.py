import time as tm

 tm.time()
 antes = tm.time()
 lista = []
 for i in range(0, 100000):
     lista.append(i)
 depois = tm.time()

 intervalo = depois - antes
 print(intervalo)

 print('Finalizando...')
 tm.sleep(2)
print('...')
tm.sleep(2)
print('Até a próxima')
