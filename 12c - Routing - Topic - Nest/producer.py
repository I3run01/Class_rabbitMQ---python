import pika
from pika.exchange_type import ExchangeType

exchangeName = 'helloWorldExchange'

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange=exchangeName, exchange_type=ExchangeType.topic)

message = 'hello world'
channel.basic_publish(exchange=exchangeName,routing_key='hello.world', body=message)
print(message)

connection.close()