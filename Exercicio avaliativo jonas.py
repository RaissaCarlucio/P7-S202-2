import threading
import time
import random
from pymongo import MongoClient


# Exercicios tarefa avaliativa Jonas:

def sensorTemp(sensor, intervalo):
    # Gera um número aleatório entre 20 e 30 para simular a temperatura do sensor
    temperatura = random.uniform(30,40)
    print(f'Sensor {sensor}: Temperatura atual: {temperatura:.1f}°C')
    
    client = MongoClient('localhost', 27017)
    db = client['bancoiot']
    collection = db['sensores']
    #Inserindo os dados
    collection.insert_one({'sensor': sensor, 'temperatura': temperatura})
    # Pausa a execução da thread por "intervalo" segundos
    time.sleep(intervalo)

# Cria três threads com o target sendo a função sensorTemp e passando os argumentos 'Sensor1', 'Sensor2' e 'Sensor3' e intervalos.
x = threading.Thread(target = sensorTemp, args = ('Sensor1', 2))
y = threading.Thread(target = sensorTemp, args = ('Sensor2', 3))
z = threading.Thread(target = sensorTemp, args = ('Sensor3', 4))

# Inicia a execução das threads
x.start()
y.start()
z.start()

# Espera as threads terminar sua execução
x.join()
y.join()
z.join()