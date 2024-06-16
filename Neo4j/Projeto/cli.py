
from database import Database
from player_crud import PlayerCRUD
from character_crud import CharacterCRUD
from query_character import Character_query
from query import Query

class CLI:
    def __init__(self, database):
        self.player_crud = PlayerCRUD(database)
        self.character_crud = CharacterCRUD(database)
        self.query = Query(database)
    
        

    def menu(self):
        print("Bem-vindo ao Menu!")
        while True:
            print("\nEscolha uma opção:")
            print("[1] Criar jogador")
            print("[2] Pesquisar jogador")
            print("[3] Atualizar nível do jogador")
            print("[4] Deletar jogador")
            print("[5] Criar personagem")
            print("[6] Pesquisar personagem")
            print("[7] Atualizar classe do personagem")
            print("[8] Deletar personagem")
            print("[9] Calcular nível médio dos jogadores")
            print("[10] Calcular nível total dos inimigos")
            print("[11] Sair")
            s = input("Digite o número da opção desejada: ")
            
            if s == "1":
                self.create_player()
            elif s == "2":
                self.read_player()
            elif s == "3":
                self.update_player()
            elif s == "4":
                self.delete_player()
            elif s == "5":
                self.create_character()
            elif s == "6":
                self.read_character()
            elif s == "7":
                self.update_character()
            elif s == "8":
                self.delete_character()
            elif s == "9":
                self.average_player_level()
            elif s == "10":
                self.total_enemy_levels()    
            elif s == "11":
                break
            else:
                print("Opção inválida, tente novamente.")

    def create_player(self):
        name = input("Nome do jogador: ")
        level = int(input("Nível do jogador: "))
        city = input("Cidade do jogador: ")
        self.player_crud.create(name, level, city)
        print(f"Jogador {name} criado com sucesso!")

    def read_player(self):
        name = input("Nome do jogador a ser pesquisado: ")
        player = self.player_crud.read(name)
        if player:
            print(f"Nome: {player['name']}, Nível: {player['level']}, Cidade: {player['city']}")
        else:
            print("Jogador não encontrado.")

    def update_player(self):
        name = input("Nome do jogador a ser atualizado: ")
        new_level = int(input("Novo nível do jogador: "))
        self.player_crud.update(name, new_level)
        print(f"Nível do jogador {name} atualizado com sucesso!")

    def delete_player(self):
        name = input("Nome do jogador a ser deletado: ")
        self.player_crud.delete(name)
        print(f"Jogador {name} deletado com sucesso!")

    def create_character(self):
        character_name = input("Nome do personagem: ")
        character_class = input("Classe do personagem: ")
        player_name = input("Nome do jogador dono do personagem: ")
        self.character_crud.create(character_name, character_class, player_name)
        print(f"Personagem {character_name} criado com sucesso!")

    def read_character(self):
        character_name = input("Nome do personagem a ser pesquisado: ")
        character = self.character_crud.read(character_name)
        if character:
            print(f"Nome: {character['name']}, Classe: {character['class']}")
        else:
            print("Personagem não encontrado.")

    def update_character(self):
        character_name = input("Nome do personagem a ser atualizado: ")
        new_class = input("Nova classe do personagem: ")
        self.character_crud.update(character_name, new_class)
        print(f"Classe do personagem {character_name} atualizada com sucesso!")

    def delete_character(self):
        character_name = input("Nome do personagem a ser deletado: ")
        self.character_crud.delete(character_name)
        print(f"Personagem {character_name} deletado com sucesso!")

    # Funcoes de Agregacao:
    def average_player_level(self):
        avg_level = self.query.average_player_level()
        print(f"Nível médio dos jogadores: {avg_level}")
    
    def total_enemy_levels(self):
        total_level = self.query.total_enemy_levels()
        print(f"Nível total dos inimigos: {total_level}")
     
                  