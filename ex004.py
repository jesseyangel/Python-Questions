############### O jeito que fiz ###############

"""num = int(input('Digite um número para ver a tabuada: '))
print('-' * 12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-' * 12)
"""


############### Metodo que aprendi pesquisando ###############



print ('Escolha um numero para ver a tabuada')

tabuada = int(input('Tabuada do número: '))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))
    1
