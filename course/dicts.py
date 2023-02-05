'''Dicionários'''

dicionario = {
    'nome': None,
    'idade': None
    }

print(dicionario.keys())

nome = input('Digite um nome: ')
idade = int(input('Digite uma idade: '))

dic_transicao = {
    'nome': nome,
    'idade': idade
}

dicionario.update(dic_transicao)

print(f'{dicionario["nome"]} tem {dicionario["idade"]} anos.')
