import json, os, django
import pika

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()
from products.models import Product

params = pika.URLParameters('amqps://ttznihfm:RBPAvUtWT1AqIz4fA3NVwnEHx1H5L6f-@puffin.rmq2.cloudamqp.com/ttznihfm')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, methods, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes+1
    product.save()
    print('Products likes increased')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()