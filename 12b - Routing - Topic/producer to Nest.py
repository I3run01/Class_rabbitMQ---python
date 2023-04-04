import pika
from pika.exchange_type import ExchangeType

# Start -> Open connection
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
# Finish the open connection step

# Queue declares
channel.queue_declare(queue='myQueue', durable=False)
# Queue declares

# Message and bind
userPaymentMessage = 'Hello world'
channel.basic_publish(exchange='', routing_key='myQueue', body=userPaymentMessage, properties=pika.BasicProperties(delivery_mode=2,))
print(f"Hello world")
# Message and bind

connection.close()
