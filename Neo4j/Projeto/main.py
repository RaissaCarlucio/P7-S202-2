from database import Database
from player_crud import PlayerCRUD
from character_crud import CharacterCRUD
from query_character import Character_query
from query import Query
from cli import CLI

# Cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.202.28.32:7687", "neo4j", "spacers-rhythms-electrolytes")

# Criando as instancias da classe para auxiliar no codigo
player_crud = PlayerCRUD(db)
character_crud = CharacterCRUD(db)
query = Query(db)
query_character = Character_query(db)


# Chamando os metodos:

# Lista de nomes dos jogadores
player_names = ["Adrian", "Raissa", "Miguel"]

# Buscando o nome do personagem e nome da classe a partir do nome do jogador
results = query.get_player_characters(player_names)

for result in results:
     print(f"Informações sobre o personagem de {result['playerName']}:")
     print(f"Nome do personagem: {result['characterName']}")
     print(f"Classe do personagem: {result['characterClass']}")
     print()


# Utilizando a classe query: 
print("Buscar o nome dos personagens que nasceram na cidade dos humanos:", query.get_players_born_in_city("City of Humans"))
print("\n")

print("Buscando as cidades em que os viloes estao:", query.get_enemy_cities())
print("\n")

print("Buscando os niveis dos inimigos:", query.get_enemy_levels())
print("\n")

# Funcoes de Agregacao:
print("Buscando o nivel medio dos jogadores: ", query.average_player_level())
print("\n")

print("Buscando o nivel total dos inimigos: ", query.total_enemy_levels())
print("\n")


# Utilizando a classe character_crud:
print("Personagens e classe do jogador Adrian: ",  query_character.get_characters_by_player())
print("\n")

character_class = "Atiradora"  # Substitua pela classe desejada
characters = query_character.get_characters_by_class(character_class)

# print(f"Personagens da classe '{character_class}':")
for player_name, character_name in characters:
    print(f"Jogador: {player_name}, Personagem: {character_name}")
print("\n")

#  Orcs
#  Dragons
#  Dwarves
#  Fairies
#  Humans

# Criando um jogador e associando um personagem a ele
player_crud.create("Emilia", 4, "City of Humans")
character_crud.create("Katarina", "Assassino", "Emilia")

# # Atualizando o personagem, alterando sua classe
character_crud.update("Katarina", "Mago")

# # Lendo o jogador
jogador_read = player_crud.read("Emilia")
print(jogador_read)

# # Lendo o personagem Zed
personagem_read = character_crud.read("Katarina")
print(personagem_read)

# Excluindo o personagem
# character_crud.delete("Zed")

# Realizando o CLI para criar, ler, dar update e deletar um professor da escolha do usuario:
if __name__ == "__main__":
    cli = CLI(db)
    cli.menu()
