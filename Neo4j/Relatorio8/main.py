from database import Database
from futebol_database import FutebolDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.86.197.22:7687", "neo4j", "yolk-courtesy-drop")
db.drop_all()

# Criando uma instância da classe FutebolDatabase para interagir com o banco de dados
futebol_db = FutebolDatabase(db)

# Criando jogadores. Passar o id primeiro
futebol_db.create_player(1, "Adrian")
futebol_db.create_player(2, "Raissa")
futebol_db.create_player(3, "Miguel")

# Criando partidas. Id da partida, resultado, id do jogador
futebol_db.create_match(1, "2-1", [1,2])  # Jogador 1 fez 2 gols e o jogador 2 fez 1 gol.
futebol_db.create_match(2, "Empate", [3,2])  # Resultado do jogo entre os jogadores 3 e 2 deu Empate.
futebol_db.create_match(2, "7-1", [1,3])  # Jogador 1 fez 7 gols e o jogador 3 fez 1 gol.

# Atualizando o nome do jogador 3
futebol_db.update_player("Miguel", "Guilherme")

# Deletando um jogador
futebol_db.delete_player(3, "Guilherme")

# Imprimindo todas as informações do banco de dados
print("Jogadores:")
print(futebol_db.get_players())
print("Partidas:")
print(futebol_db.get_matchs())
