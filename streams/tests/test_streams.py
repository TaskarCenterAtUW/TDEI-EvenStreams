from ..streams.producer import Producer
from ..streams.confluent_producer import ConfluentProducer
from ..streams.consumer import Consumer
from ..streams.confluent_consumer import ConfluentConsumer

import random
from configparser import ConfigParser

def test_streams():
    config_parser = ConfigParser()
    config_parser.read('getting_started.ini')
    config = dict(config_parser['default'])

    producer: Producer = ConfluentProducer('test', config)

    config.update(config_parser['consumer'])
    consumer: Consumer = ConfluentConsumer('test', config)
    
    msg = str(random.random())
    print(msg)

    pass