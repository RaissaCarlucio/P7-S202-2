class PlayerCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, level, city):  # cria um Jogador com seu nome, seu nível e sua cidade
        query = "CREATE (:Player{name: $name, level: $level, city: $city})"
        parameters = {"name": name, "level": level, "city": city}
        self.db.execute_query(query, parameters)

    def read(self, name):  # Lendo o jogador
        query = """
        MATCH (p:Player {name: $name}) 
        RETURN p.name AS name, p.level AS level, p.city AS city"""
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return results[0] if results else None

    def delete(self, name):  # deleta um Jogador pelo seu nome
        query = """
        MATCH (p:Player {name: $name})
        DELETE p
        """
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        
    def update(self, name, new_level):  # Atualiza o nível do jogador
        query = """
        MATCH (p:Player{name: $name})
        SET p.level = $new_level
        """
        parameters = {"name": name, "new_level": new_level}
        self.db.execute_query(query, parameters)
