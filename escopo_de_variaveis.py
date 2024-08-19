"""escopo de variaveis
dois casos de escopo

1- variaveis globais
    são reconhecidas, ou seja, seu escopo compreende
    todo o programa.

2-  variaveis locais
    são reconhecidas apenas no bloco foram declaradas, ou seja
    seu escopo esta limitado ao bloco onde foi declarado.

para declarar variaveis em python fazemos
nome_da_varial = valor_da_variavel

pythom é uma linguagem de tipagem dinamica
aod declarar uma variavel, não colocamos o tipo de dado dela
este tipo é inferido ao atribuimos o valor a mesma"""


numero = 55 #variavel global
print(numero)

numero = 55
#escopo local = 0
if numero < 60:
    novo = numero + 10 # a variavel novo esta declarada localmente dentro do bloco do if #portanto é local
    print(novo)



