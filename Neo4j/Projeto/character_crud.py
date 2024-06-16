class CharacterCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, character_name, character_class, player_name):  # Nome do personagem, classe, nome do jogador
        query = """
        MATCH (p:Player {name: $player_name})
        CREATE (p)-[:PERSONAGEM_NO_RPG]->(:Character {name: $character_name, class: $character_class})
        """
        parameters = {"character_name": character_name, "character_class": character_class, "player_name": player_name}
        self.db.execute_query(query, parameters)

    def read(self, character_name): # Lendo o personagem do jogador
        query = """
        MATCH (:Player)-[:PERSONAGEM_NO_RPG]->(c:Character {name: $character_name}) 
        RETURN c.name AS name, c.class AS class
        """
        parameters = {"character_name": character_name}
        result = self.db.execute_query(query, parameters)
        return result[0] if result else None
    
    def delete(self, character_name): # Deletando o personagem
        query = """
        MATCH (:Player)-[:PERSONAGEM_NO_RPG]->(c:Character {name: $character_name}) 
        DELETE c
        """
        parameters = {"character_name": character_name}
        self.db.execute_query(query, parameters)

    def update(self, character_name, new_class): # Atualiza a classe do personagem
        query = """
        MATCH (:Player)-[:PERSONAGEM_NO_RPG]->(c:Character {name: $character_name}) 
        SET c.class = $new_class
        """
        parameters = {"character_name": character_name, "new_class": new_class}
        self.db.execute_query(query, parameters)
