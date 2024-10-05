def kadane(arr):
    max_atual = arr[0]
    max_global = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > max_atual + arr[i]:
            max_atual = arr[i]
            s = i
        else:
            max_atual += arr[i]

        if max_atual > max_global:
            max_global = max_atual
            start = s
            end = i

    return max_global, arr[start:end+1]

def totalCumulativo(arr):
    arrayCumulativo = []
    cumulativo = 0
    for num in arr:
        cumulativo += num
        arrayCumulativo.append(cumulativo)
    return arrayCumulativo

def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Valor Invalido, Digite um Numero")

# Solicita ao usuário para digitar o número de elementos
n = get_valid_integer("Quantos números você deseja digitar? ")

# Inicializa uma lista vazia para armazenar os números
arr = []

# Solicita ao usuário para digitar cada número individualmente
print("Digite um Numero de Cada Vez!")
for i in range(n):
    num = get_valid_integer(f"Digite o {i + 1}° Numero: ")
    arr.append(num)

# Verifica se a lista não está vazia
if arr:
    # Calcula a soma acumulativa
    arrayCumulativo = totalCumulativo(arr)
    
    # Aplica o algoritmo de Kadane
    resultado, subarray = kadane(arr)
    
    # Exibe os resultados
    print("As cumulativas são:", arrayCumulativo)
    print("A soma máxima da subarray é:", resultado)
    print("O subarray com a soma máxima é:", subarray)
else:
    print("Você precisa digitar pelo menos um número.")
