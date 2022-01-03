import confluent_kafka
from ..streams.producer import Producer

class ConfluentProducer(Producer):
    def __init__(self, topic: str, config: dict):
        self.producer = confluent_kafka.Producer(config)
        self.topic = topic

    def produce(self, key: str, value: str):
        self.producer.produce(self.topic, key, value,
                callback=__delivery_callback__)

        # self.producer.poll(10000)
        # self.producer.flush()
    
    def __delivery_callback__(err, msg):
        if err:
            """Error has occured, resolve"""
        else:
            """Message was written to stream successfully"""
