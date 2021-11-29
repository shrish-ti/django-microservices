import pika, json

params = pika.URLParameters('amqps://ttznihfm:RBPAvUtWT1AqIz4fA3NVwnEHx1H5L6f-@puffin.rmq2.cloudamqp.com/ttznihfm')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)

