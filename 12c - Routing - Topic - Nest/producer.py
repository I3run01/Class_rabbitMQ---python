import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

exchange_name = 'helloWorldExchange'
routing_key = 'hello.world'
queue_name = 'myQueue'

channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=False)

message = 'Hello, world!'
channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)

print(f'Sent message: {message}')

connection.close()
