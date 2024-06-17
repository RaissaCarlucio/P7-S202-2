import redis
import time
#pip install redis


redis_conn = redis.Redis(
    host="redis-18299.c10.us-east-1-2.ec2.redns.redis-cloud.com", 
    port=18299,
    username="default", # use your Redis user. More info https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/
    password="xamBIKIVlT049sy7UU9ZzR5DHkU6B99j", # use your Redis password
    decode_responses=True
)

# Crie um sistema de cache para um sistema de mensagens online
# Nesse sistema voce deve manter os dados dos ususarios (id, nome e email) alem dos dados da mensagem (id, hora, data, conteudo, remente e destinatario)
# Os usuarios vem ficar registrados por no maximo 1 minuto sem interacao, depois disso seu registro deve ser excluido
# As mensagens devem ser apagadas depois de 5 segundos
# Crie uma demonstracao em Python para exibir uma conversa entre dois usuarios




# Hset = Usado para colocar somente por exemplo no product 1. 
# Hmset = usado para colocar em varios produtos

class CacheSystem:
    def __init__(self):
        self.user_cache_time = 60  # Tempo de expiração dos usuários em segundos (1 minuto)
        self.message_cache_time = 5  # Tempo de expiração das mensagens em segundos (5 segundos)

    def add_user(self, user_id, name, email):
        user_key = f"user:{user_id}"
        user_data = {"id": user_id, "name": name, "email": email}
        redis_conn.hmset(user_key, user_data) # Ele permite inserir ou atualizar vários campos simultaneamente dentro de uma estrutura de dados hash.
        redis_conn.expire(user_key, self.user_cache_time) #  Isso significa que após o tempo especificado, a chave será automaticamente removida pelo Redis do armazenamento.

    def add_message(self, message_id, timestamp, content, sender_id, recipient_id):
        message_key = f"message:{message_id}"
        message_data = {
            "id": message_id,
            "timestamp": timestamp,
            "content": content,
            "sender_id": sender_id,
            "recipient_id": recipient_id
        }
        redis_conn.hmset(message_key, message_data)
        redis_conn.expire(message_key, self.message_cache_time)

    def get_user(self, user_id):
        user_key = f"user:{user_id}"
        return redis_conn.hgetall(user_key)

    def get_message(self, message_id):
        message_key = f"message:{message_id}"
        return redis_conn.hgetall(message_key)


# Demo para exibir uma conversa entre dois usuários
def main():
    cache_system = CacheSystem()

    # Adiciona alguns usuários
    cache_system.add_user(1, "Alice", "alice@example.com")
    cache_system.add_user(2, "Bob", "bob@example.com")

    # Envia mensagens entre os usuários
    cache_system.add_message(1, time.time(), "Olá Bob, tudo bem?", 1, 2)
    cache_system.add_message(2, time.time(), "Oi Alice, estou bem e você?", 2, 1)
    cache_system.add_message(3, time.time(), "Estou bem também!", 1, 2)

    # Exibe a conversa entre Alice e Bob
    print("Conversa entre Alice e Bob:")
    for message_id in range(1, 4):
        message = cache_system.get_message(message_id)
        sender_name = cache_system.get_user(message['sender_id'])['name']
        recipient_name = cache_system.get_user(message['recipient_id'])['name']
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(message['timestamp'])))
        print(f"{timestamp} - {sender_name} para {recipient_name}: {message['content']}")


if __name__ == "__main__":
    main()
