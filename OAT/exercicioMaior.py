# Solicitar 5 números ao usuário
# Descobrir o menor número
# Descobrir o Maior número

numero = []

for i in range(5):
    num = int(input(f"Digite o {i+1} número: "))
    numero.append(num)
    
menor = min(numero)
maior = max(numero)

print(f"O menor numero foi {menor}")
print(f"O maior numero foi {maior}")