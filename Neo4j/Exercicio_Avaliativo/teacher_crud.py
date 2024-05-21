class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf): # cria um Teacher
        query = "CREATE (:Teacher{name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)
    
    def read(self, name): # retorna apenas um Teacher
        query = """
        MATCH (t:Teacher {name: $name})
        RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return results[0] if results else None
    
    def delete(self, name): # deleta Teacher com base no name
        query = """
        MATCH (t:Teacher {name: $name})
        DELETE t
        """   
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def update(self, name, new_cpf): # atualiza cpf com base no name  
        query = """
        MATCH (t:Teacher{name: $name})
        SET t.cpf = $new_cpf
        """
        parameters = {"name": name, "new_cpf": new_cpf}
        self.db.execute_query(query, parameters)   

