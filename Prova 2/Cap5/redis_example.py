import redis 
#pip install redis



redis_conn = redis.Redis(
    host="redis-18299.c10.us-east-1-2.ec2.redns.redis-cloud.com", 
    port=18299,
    username="default", # use your Redis user. More info https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/
    password="xamBIKIVlT049sy7UU9ZzR5DHkU6B99j", # use your Redis password
    decode_responses=True
)

# redis_conn.hset("product:2", mapping={
#     "nome": "Macbook",
#     "preco": 12999.99,
#     "marca": "Apple",
#     "descricao": "Um notebbok simples de entrada"
# })

# redis_conn.lpush("estoque", "poduct:1","product:2")

redis_conn.lrem("estoque", 1,"poduct:1" )
# redis_conn.lpush("estoque", "product:1")

tamanho_estoque = redis_conn.llen("estoque")

estoque = redis_conn.lrange("estoque", 0, tamanho_estoque-1)
print(estoque)
for produto in estoque:
    print(redis_conn.hget(produto, "nome"))
    print(redis_conn.hget(produto, "preco"))
    print()