import random

print('Bem vindo ao teu gerador de Password ')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?'

number = input('Quantidade de password para gerar? ')
number = int(number)

length = input('Qual o tamanho da Password ')
length = int(length)

print('\n Aqui estão as tuas password: ')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)

