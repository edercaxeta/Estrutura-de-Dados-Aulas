def kadane(arr):
    max_atual = arr[0]
    max_global = arr[0]
    
    for i in range(1, len(arr)):
        max_atual = max(arr[i], max_atual + arr[i])
        if max_atual > max_global:
            max_global = max_atual
    
    return max_global

# Solicita ao usuário para digitar os números, separados por espaço
entrada = input("Digite os números, separados por espaço: ")

# Converte a entrada do usuário em uma lista de inteiros
arr = list(map(int, entrada.split()))

# Verifica se a lista não está vazia
if arr:
    resultado = kadane(arr)
    print("A soma máxima da sublista é:", resultado)
else:
    print("Você precisa digitar pelo menos um número.")