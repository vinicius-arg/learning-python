nome = input('Qual o seu nome?\n');
print('Olá,', nome);

sobrenome = input('Qual o seu sobrenome?\n');
idade = input('Qual a sua idade?\n');

print(nome, sobrenome, idade);

n1 = int(input('Digite um número: '));
n2 = int(input('Digite outro número: '));

print('A soma entre', n1, 'e', n2, 'é', n1 + n2);

product = 20
tax = 0.10
price = product * (1 + tax)

print(price)

# números complexos

calc_complex = (5+3j) + (4+2j)
print(calc_complex)

print(complex(10,2))

# strings

string = 'doesn\'t'
print(string)
print(r'\a\n\r')

literal = '''\
                        welcome, _______
    user ----------------------------------- vinicius-arg
    password ------------------------------- 12345678
    email ---------------------------------- tantantan@gmail.com
'''
print(literal)

chika = 5 * 'shuki ' + 'setee'
print(chika)

name = 'Back yi-jin'
print(name[:5] + name[5:])

other_name = 'N' + name[1:]
print(other_name)

print(len(name))

#listas

squares = [1, 4, 9, 16, 25]

# new_squares = squares
# new_squares.append(36)
# print(new_squares)
# print(squares)
# o valor foi passado como referência, em vez disso:

new_squares = squares[:]
new_squares.append(36)
print(new_squares)

squares[:2] = ['um', 'quatro']
print(squares)

print(len(squares))