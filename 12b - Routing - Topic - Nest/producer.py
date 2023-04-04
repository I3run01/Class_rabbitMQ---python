import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='MATH_SERVICE', exchange_type=ExchangeType.topic)

message = 'hello world'
channel.basic_publish(exchange='MATH_SERVICE',routing_key='hello.world', body=message)
print(message)

connection.close()