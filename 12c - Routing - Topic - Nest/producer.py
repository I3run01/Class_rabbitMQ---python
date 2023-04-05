import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

exchange_name = 'helloWorldExchange'
routing_key = 'hello.world'
queue_name = 'myQueue'

channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=False)

message = 'Hello, world!'
channel.basic_publish(
    exchange=exchange_name, 
    routing_key=routing_key, 
    body=message, 
    properties=pika.BasicProperties(
        app_id='userService',
        content_type='application/json',
        content_encoding='utf-8',
        delivery_mode=2,
    ),
)

print(f'Sent message: {message}')

connection.close()
