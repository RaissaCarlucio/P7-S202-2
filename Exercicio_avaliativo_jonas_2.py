from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def create_and_return_example(tx, code, test_data):
    query = """
        CREATE (n:TEST {
            description: $test_data,
            code: $code
        })
    """
    result = tx.run(query, test_data=test_data, code=code)
    try:
        return [{"test_data": row["n"]["description"]} for row in result]
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

def get_amount_data(tx):
    query = """
        MATCH (n) RETURN COUNT(n) AS amount;
    """
    try:
        result = tx.run(query)
        return [{'amount': row['amount']} for row in result]
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

def run_query(tx, cypher_query):
    result = tx.run(cypher_query)
    return [{"result": row} for row in result]

uri = "bolt://35.173.247.98:7687"
user = "neo4j"
password = "currents-malfunction-moistures"

driver = GraphDatabase.driver(uri, auth=(user, password))

code = 2
test_data = "Creating a new node..."

with driver.session() as session:
    session.write_transaction(create_and_return_example, code, test_data)

with driver.session() as session:
    result = session.read_transaction(get_amount_data)
    print("Número total de nós no grafo:", result[0]['amount'])

questions = [
    "Qual o tipo de relacionamento do druida com o paladino?",
    "Qual é a especialidade, música preferida e experiência do Sacerdote que é conselheiro e gosta de Rock?",
    "Qual o tipo de relacionamento do atirador de pistola com o mago de agua?",
]

for question in questions:
    print("\n" + question)
    cypher_query = ""
    if question == "Qual o tipo de relacionamento do druida com o paladino?":
        cypher_query = """
            MATCH (d:Personagem:Druida)-[r]->(p:Personagem:Paladino)
            RETURN type(r)
        """
    elif question == "Qual é a especialidade, música preferida e experiência do Sacerdote que é conselheiro e gosta de Rock?":
        cypher_query = """
            MATCH (p:Personagem:Sacerdote)
            WHERE p.especialidade = "Coselheiro" AND p.musicapreferida = "Rock"
            RETURN p.especialidade AS especialidade, p.musicapreferida AS musicapreferida, p.experiencia AS experiencia
        """
    elif question == "Qual o tipo de relacionamento do atirador de pistola com o mago de agua?":
        cypher_query = """
            MATCH (d:Personagem:Atirador{especialidade:"Pistola"})-[r]->(p:Personagem:Mago{especialidade:"Agua"})
            RETURN type(r)
        """    
    with driver.session() as session:
        result = session.read_transaction(run_query, cypher_query)
        print(result)


driver.close()
