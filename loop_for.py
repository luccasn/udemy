'''loop é uma estrutura de repetição

For é uma dessas estruturas

C ou Java

For(int i = 0; i < limitador; i++){
//execução do loop
}

Python
for iten in interavel:
    //execução do loop

utilzamos loops para iterar sobre sequencias ou sobre valores iteraveis
Ex de iteraveis
- string
    nome = 'luccas'
- Lista
    lista = [1, 3, 6, 9]
-Range
    numero = range(1, 10)

  nome = 'luccas teste'
lista = [1, 2, 5, 14]
numeros = range (1, 10) # temos que transformar em lista
#ex de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

#ex de for 2 iterando sobre uma lista
for numeros in lista:
    print(numeros)

# ex de for 3(iterando sobre um range)
#range (valor_inicial, valor_final -1
#o valor final não é inclusive
for numeros in range (1, 10):
    print(numeros)

#for indice, letra in enumerate(nome):
#print(nome[indice])
for _, letra in enumerate(nome): #pode ser usado o underline para descartar o valor
    print(letra)
for valor in enumerate(nome):
    print(valor)

nome = 'teste python '
for letra in nome:
    print(letra, end= '')# end= serve para não pular linha no for
'''

qtd = int(input('quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):# o range é sempre o valor menos 1, caso queria acrescentar, coloque +1
   num = int(input(f'Informe o {n}/{qtd} valor: '))
   soma = soma + num
   print(f'A soma é {soma}')

#https://apps.timwhitlock.info/emoji/tables/unicode
#codigo original U+1F638
# modificado U0001f638 para mudar o codigo, no lugar do + colocar 3 zeros

for _ in range(3):
    for num in range(1, 5):
        print('\U0001f638 \U0001F637' * num)