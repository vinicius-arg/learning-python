'''Script simples que realiza operações em listas'''

my_list = []

n = int(input('Quantos elementos deseja inserir na lista? '))

for i in range(n):
    inserted = input(f'Insira o {i + 1}o elemento: ')
    my_list.append(inserted)

print('''
        ** Use:
0 para representar False e
 1 para representar True
''')

sort_list = bool(int(input('Ordenar lista? ')))

if sort_list is True:
    my_list.sort()
    print(f'Lista ordenada: {my_list}')

insert = bool(int(input('Inserir elemento? ')))

if insert is True:
    inserted = input('Digite o elemento a ser inserido: ')
    my_list.append(inserted)
    print(f'Lista atualizada: {my_list}')

find = bool(int(input('Buscar elemento? ')))

if find is True:
    element = input('Digite o elemento a ser buscado: ')
    if element in my_list:
        index = my_list.index(element)
        print(f'{element} ocupa a {index + 1}a posição na lista. índice [{index}]')
    else:
        print('Elemento não existe.')
