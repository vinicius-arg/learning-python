a, b, i = 0, 1, 0

count = int(input('Quantos numeros da sequencia deseja exibir? '))

while i < count:
    print(a, end=' - ')
    a, b = b, a + b
    i += 1 

print('...')