class TabelaHash:
    def __init__(self):
        self.tabela = [[] for _ in range(10)]

    def __hash(self, chave):
        return hash(chave) % len(self.tabela)

    def inserir(self, chave, valor):
        indice = self.__hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                item[1] = valor
                return
        self.tabela[indice].append([chave, valor])
    
    def buscar(self, chave):
        indice = self.__hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        return None  # Retorna None se a chave não for encontrada
    
hash_table = TabelaHash()
hash_table.inserir("nome", "João")
hash_table.inserir("idade", 25)
print(hash_table.buscar('nome'))  # Saída: João
