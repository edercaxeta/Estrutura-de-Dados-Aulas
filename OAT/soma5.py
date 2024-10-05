numero = []

for i in range(5):
    num = int(input(f"Digite o {i+1} número: "))
    numero.append(num)
    
soma = sum(numero)

print(f"A soma foi {soma}")