import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

exchange_name = 'exchangeName'
routing_key = 'hello.worlds'
queue_name = 'myQueue'

channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)

message = 'Hello, world!'
channel.basic_publish( exchange=exchange_name, pattern=routing_key, body=message, )

print(f'Sent message: {message}')

connection.close()
