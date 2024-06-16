from database import Database


class Character_query:
    def __init__(self, database):
        self.db = database

        # Buscando personagens do jogador Adrian
    def get_characters_by_player(self):
        query = """
        MATCH (p:Player {name: 'Adrian'})-[:PERTENCE_NO_RPG]->(c:Character)
        RETURN c.name AS character_name, c.class AS character_class
        """
        results = self.db.execute_query(query)
        return [(result['character_name'], result['character_class']) for result in results]

    def get_characters_by_class(self, character_class):
        query = """
        MATCH (p:Player)-[:PERTENCE_NO_RPG]->(c:Character {class: $character_class})
        RETURN c.name AS character_name, p.name AS player_name
        """
        parameters = {"character_class": character_class}
        results = self.db.execute_query(query, parameters)
        return [(result['player_name'], result['character_name']) for result in results]