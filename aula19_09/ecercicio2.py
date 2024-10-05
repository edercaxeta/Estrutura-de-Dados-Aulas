""" Crie uma lista vazia para representar a pilha.
Adicione os elementos "A", "B" e "C" à pilha. *
Exiba o item no topo da pilha (sem removê-lo).*
Remova dois itens da pilha e mostre o valor de cada um.*
Verifique o tamanho atual da pilha.*
Verifique se a pilha está vazia.*
Remova o último item e mostre o status da pilha novamente. """

pilha=[]

pilha.append("a")
pilha.append("b")
pilha.append("c")
print(pilha)

topo = pilha [-1]
print(topo)

pilha.pop()
pilha.pop()
print(pilha)

tamanhoAtual=len(pilha)
print(f"Tamanho: {tamanhoAtual}")

if len(pilha) == 0:
    print("A Pilha esta Vazia")
else:
    print("A pilha não esta Vazia")
print(pilha)

pilha.pop()

print("A pilha está vazia?",len(pilha)==0)