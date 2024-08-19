"""3. Faça um programa que recebe três
 valores e apresente a soma dos quadrados dos valores lidosbbhbh."""

valor: int = int(input("Digite o primeiro Valor inteiro:"))
print(valor)
valor2: int = int(input("Digite um segundo Valor inteiro:"))
print(valor2)
valor3: int = int(input('Digite o terceiro valor inteiro:'))
print(valor3)

soma: int = valor **2 + valor2 **2 + valor3 **2
print(f'A soma do numero elevado ao quadrado {valor} com o numero elevado ao quadrado {valor2} e o numero elevado ao quadrado'
      f' {valor3} é {soma}:')