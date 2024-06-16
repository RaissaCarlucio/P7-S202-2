from database import Database


class Query:
    def __init__(self, database):
        self.db = database

# ------------- Buscando as coisas que estao nos arquivos de texto  -------------

    def get_player_characters(self, player_names):
        results = []
        for player_name in player_names:
            query = (
                "MATCH (p:Player {name: $playerName})-[:PERTENCE_NO_RPG]->(c:Character) "
                "RETURN p.name AS playerName, c.name AS characterName, c.class AS characterClass"
            )
            parameters = {"playerName": player_name}

            result = self.db.execute_query(query, parameters)
            results.extend(result)

        return results
    # Buscar o nome dos personagens que nasceram na cidade dos humanos
    def get_players_born_in_city(self, city_name):
        query = """
        MATCH (p:Player)-[:NASCEU_EM]->(c:City{name: $city_name})
        RETURN p.name AS player_name
        """
        parameters = {"city_name": city_name}
        results = self.db.execute_query(query, parameters)
        return [result['player_name'] for result in results]
    
    # Buscando as cidades em que os vilões estão   
    def get_enemy_cities(self):
        query = """
        MATCH (e:Enemy)-[:RESIDE_EM]->(c:City)
        RETURN c.name AS city_name
        """
        results = self.db.execute_query(query)
        return [result['city_name'] for result in results]
    
    # Buscando os níveis dos inimigos
    def get_enemy_levels(self):
        query = """
        MATCH (e:Enemy)
        RETURN e.name AS enemy_name, e.level AS enemy_level
        """
        results = self.db.execute_query(query)
        return [(result['enemy_name'], result['enemy_level']) for result in results]

# ------------------- Funcoes de Agregacao -------------------
    # Buscando o nivel medio dos jogadores
    def average_player_level(self):
        query = """
        MATCH (p:Player)
        RETURN AVG(p.level) AS average_level
        """
        results = self.db.execute_query(query)
        return results[0]['average_level'] if results else None
    
    # Buscando o nivel total dos inimigos
    def total_enemy_levels(self):
        query = """
        MATCH (e:Enemy)
        RETURN SUM(e.level) AS total_level
        """
        results = self.db.execute_query(query)
        return results[0]['total_level'] if results else None