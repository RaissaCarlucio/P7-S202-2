class PlayerCRUD:
    def __init__(self, database):
        self.db = database

    # Cria um jogador com seu nome, nivel e cidade
    def create(self, name, level, city):  
        query = "CREATE (:Player{name: $name, level: $level, city: $city})"
        parameters = {"name": name, "level": level, "city": city}
        self.db.execute_query(query, parameters)

    # Lendo o jogador
    def read(self, name):  
        query = """
        MATCH (p:Player {name: $name}) 
        RETURN p.name AS name, p.level AS level, p.city AS city"""
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return results[0] if results else None

    # Deletando um jogador
    def delete(self, name):  
        query = """
        MATCH (p:Player {name: $name})
        DELETE p
        """
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        
    # Atualiza o nivel do jogador    
    def update(self, name, new_level):  
        query = """
        MATCH (p:Player{name: $name})
        SET p.level = $new_level
        """
        parameters = {"name": name, "new_level": new_level}
        self.db.execute_query(query, parameters)
