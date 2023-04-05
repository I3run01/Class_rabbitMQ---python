import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

exchange_name = 'exchangeName'
routing_key = 'hello.world'

channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)

message = 'Hello, world!'
channel.basic_publish( exchange=exchange_name, routing_key=routing_key, body=message )

print(f'Sent message: {message}')

connection.close()
