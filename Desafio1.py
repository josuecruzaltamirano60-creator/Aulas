print('Cadastro dos 3 Clientes')
nome1 = input('Nome do Cliente 1: ')
idade1 = int(input('Idade do Cliente 1'))
nome2 = input('Nome do Cliente 2: ')
idade2 = int(input('Idade do Cliente 2'))
nome3 = input('Nome do Cliente 3: ')
idade3 = int(input('Idade do Cliente 3'))

# Preços
Simples = 100
Duplo = 150
Luxo = 250

print('Ecolha do quarto digite o nome do quarto')

quarto1 = input(f"{nome1}, escolha o quarto: ")
quarto2 = input(f"{nome2}, escolha o quarto: ")
quarto3 = input(f"{nome3}, escolha o quarto: ")

# Dias
print("\n3. QUANTOS DIAS?")
dias1 = int(input(f"{nome1} ficará quantos dias? "))
dias2 = int(input(f"{nome2} ficará quantos dias? "))
dias3 = int(input(f"{nome3} ficará quantos dias? "))

# Calculo
# Cliente 1
if quarto1 == "Simples":
    valor1 = dias1 * Simples
elif quarto1 == "Duplo":
    valor1 = dias1 * duplo
else:
    valor1 = dias1 * luxo  # Luxo

# Cliente 2
if quarto2 == "Simples":
    valor2 = dias2 * Simples
elif quarto2 == "Duplo":
    valor2 = dias2 * duplo
else:
    valor2 = dias2 * luxo

# Cliente 3
if quarto3 == "Simples":
    valor3 = dias3 * simples
elif quarto3 == "Duplo":
    valor3 = dias3 * duplo
else:
    valor3 = dias3 * luxo

# resumo
print("\n" + "="*45)
print("       RESUMO DAS RESERVAS")
print("="*45)

print(f"\n{nome1} ({idade1} anos)")
print(f"  Quarto: {quarto1}")
print(f"  Diárias: {dias1}")
print(f"  Total: R$ {valor1:.2f}")

print(f"\n{nome2} ({idade2} anos)")
print(f"  Quarto: {quarto2}")
print(f"  Diárias: {dias2}")
print(f"  Total: R$ {valor2:.2f}")

print(f"\n{nome3} ({idade3} anos)")
print(f"  Quarto: {quarto3}")
print(f"  Diárias: {dias3}")
print(f"  Total: R$ {valor3:.2f}")

print("\n" + "-"*45)
print(f"TOTAL GERAL: R$ {valor1 + valor2 + valor3:.2f}")
print("-"*45)
