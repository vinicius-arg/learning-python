'''Script simples que realiza operações em listas'''

my_list = []

# in order: blue, red, white; all bold except white
colors = ['\033[34m' + '\033[1m', '\033[31m' + '\033[1m', '\033[0;0m']

n = int(input('Quantos elementos deseja inserir na lista? '))

for i in range(n):
    inserted = input(f'Insira o {i + 1}o elemento: ')
    my_list.append(inserted)

print(colors[0] + '''
        ** Use:
0 para representar False e
 1 para representar True
''' + colors[2])

sort_list = bool(int(input('Ordenar lista? ')))

if sort_list is True:
    my_list.sort()
    print(colors[0] + f'Lista ordenada: {my_list}' + colors[2])

insert = bool(int(input('Inserir elemento? ')))

if insert is True:
    inserted = input('Digite o elemento a ser inserido: ')
    my_list.append(inserted)
    print(colors[0] + f'Lista atualizada: {my_list}' + colors[2])

find = bool(int(input('Buscar elemento? ')))

if find is True:
    element = input('Digite o elemento a ser buscado: ')
    if element in my_list:
        index = my_list.index(element)
        print(colors[0] + f'{element} ocupa a {index + 1}a posição na lista. índice [{index}]' + colors[2])
    else:
        print(colors[1] + 'Elemento não existe.' + colors[2])
