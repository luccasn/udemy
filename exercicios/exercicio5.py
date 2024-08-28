"""2. Faça um programa que leia um número inteiro fornecido pelo usuário.
Se esse número for positivo, calcule a raiz quadrada do número e apresente-a.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido."""

from math import sqrt # from math import serve para importar a biblioteca para que possa fazer operações matematicas

num: int = int(input('Digite um número inteiro: '))
if num > 0:
    print(f'A raiz quadrada {num} é {sqrt(num)}')
else:
    print(f'O número {num} é inválido')

