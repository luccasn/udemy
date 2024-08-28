"""3. Faça um programa que recebe um número inteiro
e informe se este número é par ou ímpar."""

num: int = int(input('Digite um número: '))
if num % 2 == 0: #você usa o sinal % para ter o resto da divisão de um número por 2 vai ser igual
    # a 0 caso ele seja par
    print(f'Este número {num} é par')
else:
    print(f'Este número {num} é impar') #testanto commit
