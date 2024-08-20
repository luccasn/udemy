"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

"""
num: int = int (input('Informe um número: ')) #num recebe = numero inteiro input mostra ao ususario
num2: int = int (input('Informe um outro número'))

if num > num2:
    print(f'o primeiro número{num} é maior que {num2}')
elif num == num2:
    print(f'Os números {num} e {num2} são iguais.')
else:
    print(f'O segundo número {num2} é maior que {num}')