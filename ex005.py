num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1): #+1 pq o python sempre conta 1 a menos dentro do for
    if num % c == 0: #se nume for divisivel pelo contador
        print('\033[33m', end='') #mostre com cor yellow
        tot += 1 #total mais ou igual a 1
    else:
        print('\033[31m', end='') #senao mostre com cor red
    print('{} '.format(c), end='')

print(f'\n\033m O número {num} foi divisível {tot} vezes')
if tot == 2: #Se for igual a 2 
    print(f'\032 por isso ele É PRIMO!')
else: #senao for igual a 2
    print(f'\032 isso ele NÃO É PRIMO!')
