""" Atividade OAT (Mapas ou Dicionários (Maps/Dictionaries))
Utilize mapas para armazenar Informações sobre filmes (título, ano, gênero, notas). 
Eles devem permitir que o usuário busque um filme pelo título, exibindo suas informações.
Faça uma media das notas dos filmes. """


# Dicionário com os filmes
filmes = {
    "Cidade de Deus": {"Ano": 2002, "Genero": "Crime", "Nota": 8.6},   
    "Tropa de Elite": {"Ano": 2007, "Genero": "Ação", "Nota": 8.1},  
    "Central do Brasil": {"Ano": 1998, "Genero": "Drama", "Nota": 8.0},
    "O Auto da Compadecida": {"Ano": 2000, "Genero": "Comédia", "Nota": 8.6},  
    "Bacurau": {"Ano": 2019, "Genero": "Mistério", "Nota": 7.9}
}

# Função para buscar filmes pelo título
def buscaFilmes(titulo):
    if titulo in filmes:
        info = filmes[titulo]
        print(f"{titulo} - Ano: {info['Ano']}, Gênero: {info['Genero']}, Nota: {info['Nota']}")
    else:
        print(f"{titulo} não está em nosso banco de dados.")

# Função para calcular a média das notas
def mediaNota():
    somaNota = sum(filme['Nota'] for filme in filmes.values())
    media = somaNota / len(filmes)
    print(f"A soma das notas é: {somaNota:.2f}")
    print(f"A média das notas dos filmes é: {media:.2f}")


print("\n\n=====================================Biblioteca de Livros=================================")
while True:
    print("\n=======================================================================")    
    print("| Digite 1 para Buscar Filme pelo Título                              |")
    print("| Digite 2 para Calcular a Média das Notas dos Filmes                 |")
    print("| Digite 3 para Finalizar o Programa                                  |")
    print("| Digite outro valor para Voltar à Janela Inicial                     |")
    print("=======================================================================\n") 

    escolha = int(input("Escolha: "))
    
    if escolha == 1:
        print("Você escolheu Buscar Filme pelo título.")
        print("\n==================== Filmes Disponíveis ============================")    
        print("| Cidade de Deus                                                    |")
        print("| Tropa de Elite                                                    |")
        print("| Central do Brasil                                                 |")
        print("| O Auto da Compadecida                                             |")
        print("| Bacurau                                                           |")
        print("=====================================================================\n") 
        titulo = input("Digite o nome do filme para saber mais informações: ")
        buscaFilmes(titulo)

    elif escolha == 2:
        print("Você escolheu Calcular a média das notas dos filmes.")
        mediaNota()

    elif escolha == 3:
        print("Encerrando o programa.")
        break
    
    else:
        print("Escolha inválida. Voltando ao menu inicial.")
    
    resposta = input("Deseja realizar outra operação? (s/n): ").lower()

    if resposta != 's':
        print("Encerrando o programa.")
        break
