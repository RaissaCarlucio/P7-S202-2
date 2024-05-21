from database import Database

class Query:
    def __init__(self, database):
        self.db = database
        
# ------------- Questao 1 ------------- 

# Busque pelo professor “Teacher” cujo nome seja “Renzo”, retorne o ano_nasc e o CPF.
    def get_renzo(self):
        query = """
        MATCH (t:Teacher{name:'Renzo'}) 
        RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"""
        results = self.db.execute_query(query)
        return [(result['ano_nasc'], result['cpf']) for result in results]

# Busque pelos professores “Teacher” cujo nome comece com a letra “M”, retorne o name e o cpf.
    def get_Professor_letra_M(self):
        query = """
        MATCH (t:Teacher) 
        WHERE t.name STARTS WITH 'M' 
        RETURN t.name AS name, t.cpf AS cpf"""
        results = self.db.execute_query(query)
        return [(result['name'], result['cpf']) for result in results]
    
# Busque pelos nomes de todas as cidades “City” e retorne-os.    
    def get_todas_cidades(self):
        query = """
        MATCH (c:City) 
        RETURN c.name AS name"""
        results = self.db.execute_query(query)
        return [result['name'] for result in results]

# Busque pelas escolas “School”, onde o number seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da escola, o endereço e o número.
    def get_School(self):
        query = """
        Match (s:School) 
        WHERE s.number >= 150 AND s.number <= 550 
        RETURN s.name AS name, s.address AS address, s.number AS number"""
        results = self.db.execute_query(query)
        return [(result['name'], result['address'], result['number']) for result in results]  
        
# ------------- Questao 2 ------------- 
# ORDER BY t.ano_nasc DESC  -> Ordena em ordem decrescente
# ORDER BY t.ano_nasc ASC -> Ordena em ordem crescente

# Encontre o ano de nascimento do professor mais jovem.
    def get_professor_mais_velho(self):
        query = """
        MATCH (t:Teacher)
        RETURN t.ano_nasc AS ano_nasc
        ORDER BY t.ano_nasc DESC 
        LIMIT 1
        """
        results = self.db.execute_query(query)
        return results[0]['ano_nasc'] if results else None

# Encontre o ano de nascimento do professor mais velho.
    def get_professor_mais_novo(self):
        query = """
        MATCH (t:Teacher)
        RETURN t.ano_nasc AS ano_nasc
        ORDER BY t.ano_nasc ASC
        LIMIT 1
        """
        results = self.db.execute_query(query)
        return results[0]['ano_nasc'] if results else None

# Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade “population”. 
    def get_media_populacao(self):
        query = """
        MATCH (c:City)
        RETURN avg(c.population) AS average_population
        """
        results = self.db.execute_query(query)
        return results[0]['average_population'] if results else None  

# Encontre a cidade cujo CEP seja igual a “37540-000” e retorne o nome com todas as letras “a” substituídas por “A” .
# Digite o cep especificado : 37540-000
    def get_cidade_por_cep(self, cep):
        query = """
        MATCH (c:City {cep: $cep})
        RETURN c.name AS novo_nome
        """
        parameters = {"cep": cep}
        results = self.db.execute_query(query, parameters)
        return results[0]['novo_nome'] if results else None
  
# Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.    
    def get_terceiro_caractere_professor(self):
        query = """
        MATCH (t:Teacher)
        RETURN SUBSTRING(t.name, 2) AS nome_a_partir_terceiro_caractere
        """
        results = self.db.execute_query(query)
        return [result['nome_a_partir_terceiro_caractere'] for result in results]