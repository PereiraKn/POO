numero = int(input("Digite um número para ver a tabuada: "))

print(f"\n--- TABUADA DO {numero} ---")

print("\n[ ADIÇÃO ]          [ SUBTRAÇÃO ]")
for i in range(1, 11):
    soma = numero + i
    subtracao = (numero + i) - numero
    print(f"{numero} + {i:2} = {soma:2}      {numero + i:2} - {numero} = {i:2}")

print("-" * 30)

print("\n[ MULTIPLICAÇÃO ]   [ DIVISÃO ]")
for i in range(1, 11):
    multiplicacao = numero * i
    dividendo = numero * i
    divisao = dividendo / numero
    print(f"{numero} x {i:2} = {multiplicacao:2}      {dividendo:2} : {numero} = {int(divisao):2}")

print("-" * 30)
