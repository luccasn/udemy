"""tipo booleano
algebra Booleana
2 constantes verdadeiro ou falso

True = verdadeiro
False = errado

Obs, sempre com a inicial maiuscula

errado
true, false

certo
True, False
"""
ativo = False
print(ativo)

"""operações basicas
"""
#negação (not)
#fazendo a negação, se o valor for verdadeiro o resultado será falso,
#se for falso o resultado será verdadeiro. Sempre ao contrario

print(not ativo)

logado = False

#ou (or)
#é uma operação binaria, ou seja, depende de dois valores. Ou um ou outro devem ser
#verdadeiros
#True or true => True
#True or false => True
#False or True => True
#False or False => False
print(ativo or logado)

#E (and)
"""tambem é uma operação binaria, depende de dois valores
ambos os valores devem ser verdadeiro.

True and True =>True
True and False =>False
False and true =>False
False and False =>False"""

