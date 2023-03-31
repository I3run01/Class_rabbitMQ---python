import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

message = "Hello this is my first message"

channel.exchange_declare(exchange='firstexchenge', exchange_type=ExchangeType.direct)

channel.exchange_declare(exchange='secondexchenge', exchange_type=ExchangeType.fanout)

channel.exchange_bind('secondexchenge', 'firstexchenge')

message = 'This message has gone through multiple exchange'

channel.basic_publish(exchange='firstexchenge', routing_key='', body=message)

print(f"sent message: {message}")

connection.close()