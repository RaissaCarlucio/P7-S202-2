import threading
import time
import random
from pymongo import MongoClient

# Função para verificar se o sensor está alarmado
def verificarAlarme(sensor):
    client = MongoClient('localhost', 27017)
    db = client['bancoiot']
    collection = db['sensores']
    
    # Se o Sensor Alarmado for true, parar de funcionar o sensor e printar a mensagem
    sensor_data = collection.find_one({'nomeSensor': sensor})
    if sensor_data and sensor_data['sensorAlarmado']:
        print(f"Atenção! Temperatura muito alta! Verificar Sensor {sensor}!")
        return True
    return False

# Função para gerar as temperaturas dos sensores
def sensorTemp(sensor, intervalo):
    client = MongoClient('localhost', 27017)
    db = client['bancoiot']
    collection = db['sensores']
    
# Enquanto a função verificarAlarme retornar False, o loop continuará gerando valores aleatórios de temperatura, atualizando os dados no banco de dados e aguardando o intervalo de tempo especificado.
    while True:
        # Verifica se o sensor está alarmado
        if verificarAlarme(sensor):
            break
        # Plotando temperaturas aleatorias de 30 a 40 graus
        temperatura = random.uniform(30, 40)
        print(f'Sensor {sensor}: Temperatura atual: {temperatura:.1f}°C')
        
        # Verifica se a temperatura excede 38 graus, deixando o sensor alarmado.
        sensor_alarmado = False
        if temperatura > 38:
            sensor_alarmado = True
        
        # Inserindo os dados
        collection.update_one({'nomeSensor': sensor}, 
                              {'$set': {'valorSensor': temperatura, 'sensorAlarmado': sensor_alarmado}},
                              upsert=True)
        time.sleep(intervalo)

# Funcao inicial importante para definir os sensores no mongdb
def Funcao_inicial():
    client = MongoClient('localhost', 27017)
    db = client['bancoiot']
    collection = db['sensores']
    
    sensores = ['Sensor1', 'Sensor2', 'Sensor3']
    for sensor in sensores:
        collection.update_one({'nomeSensor': sensor}, {'$set': {'unidadeMedida': 'C°'}}, upsert=True)

# Chama a função inicial
Funcao_inicial()

# Cria três threads com o target sendo a função sensorTemp e passando os argumentos 'Sensor1', 'Sensor2' e 'Sensor3' e intervalos.
x = threading.Thread(target=sensorTemp, args=('Sensor1', 2))
y = threading.Thread(target=sensorTemp, args=('Sensor2', 3))
z = threading.Thread(target=sensorTemp, args=('Sensor3', 4))

# Inicia a execução das threads
x.start()
y.start()
z.start()

# Mantém o programa em execução até que todas as threads terminem
x.join()
y.join()
z.join()
