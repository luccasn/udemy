"""tipo string
é considerado tipo string sempre que:
estiver entre aspas simples 'uma string', 'a', 'True', '42.1'
estiver em aspas dulpas ''uma string'', ''a'', ''True'', ''42.1''
estiver em aspas triplas '''uma string''', '''a''', '''True''', '''42.1'''
nome = 'luccas'
print(nome)
print(type(nome))

nome = "Ginas's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nSilva'
print(nome)
print(type(nome))

print(nome.upper()) transforma tudo em maiuscula
print(nome.lower())trasforma tudo em minuscula
print(nome.split()) transforma em uma lista de strings
[ 0,   1,   2,   3,   4,   5
['l', 'u', 'c', 'c', 'a', 's',]
"""
nome = 'luccas neves'
print(nome[7:12]) #slice de string

print(nome[0:6]) #slide de string
print(nome.split()[0])
print(nome.split()[1])
"""
[::-1] comece do primeiro elemento, vá ate o ultimo elemento e inverta"""
print(nome[::-1])

print(nome.replace('a', 'u')) #replace troca as strings