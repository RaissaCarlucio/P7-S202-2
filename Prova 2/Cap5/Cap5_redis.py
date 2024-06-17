import redis 
#pip install redis


redis_conn = redis.Redis(
    host="redis-18299.c10.us-east-1-2.ec2.redns.redis-cloud.com", 
    port=18299,
    username="default", # use your Redis user. More info https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/
    password="xamBIKIVlT049sy7UU9ZzR5DHkU6B99j", # use your Redis password
    decode_responses=True
)

# Adiciona produtos ao Redis usando hashes
redis_conn.hset("product:1", mapping={
    "nome": "Smartphone X",
    "descricao": "Smartphone com tela de 6 polegadas, camera tripla e bateria de longa duracao",
    "preco": 1299.90,
    "marca": "TechTech",
    "categoria": "Celulares"
})

redis_conn.hset("product:2", mapping={
    "nome": "Macbook",
    "descricao": "Um notebook simples de entrada",
    "preco": 12999.99,
    "marca": "Apple",
    "categoria": "Celulares"
})

redis_conn.hset("product:3", mapping={
    "nome": "Smartphone Y",
    "descricao": "Smartphone com tela de 5.5 polegadas e camera dupla",
    "preco": 999.99,
    "marca": "TechTech",
    "categoria": "Celulares"
})

# Crie uma lista para armazenar os IDS dos produtos em estoque
redis_conn.lpush("estoque", "product:1", "product:2", "product:3")
# Recupe as informacoes do produto com ID 1
print(redis_conn.hgetall("product:1"))

# Verifica se o produto com ID 2 está em estoque
id_2 = redis_conn.lrange("estoque", 0, -1)

if "product:2" in id_2:
    print("O produto 'product:2' está no estoque.")
else:
    print("O produto 'product:2' não está no estoque.")
        


# Cria um conjunto ordenado para armazenar produtos por categoria e por preço
redis_conn.zadd("categoria:Celulares", {"product:1": 1299.90})
redis_conn.zadd("categoria:Celulares", {"product:2": 12999.99})
redis_conn.zadd("categoria:Celulares", {"product:3": 999.99})

# Recupera produtos da categoria 'Celulares' ordenados pelo preço
produtos_celulares = redis_conn.zrange("categoria:Celulares", 0, -1, withscores=True)

# # Imprime os produtos com seus detalhes
for produto, preco in produtos_celulares:
    nome = redis_conn.hget(produto, "nome")
    descricao = redis_conn.hget(produto, "descricao")
    print(f"Produto: {nome}, Preço: {preco}, Descrição: {descricao}")


# Recupera produtos da categoria 'Celulares' com preços entre 0 e 130000.00
precos_por_categoria = redis_conn.zrangebyscore("categoria:Celulares", 0, 130000.00)
print(precos_por_categoria)  

# Remova o produto com ID 2 do estoque
redis_conn.lrem("estoque", 1, "product:2")

# Exclua o produto com ID 3 do sistema
redis_conn.delete("product:3")


    
