import confluent_kafka

class ConfluentProducer(Producer):
    def __init__(self, topic: str, config: dict):
        self.consumer = confluent_kafka.Consumer(config)
        self.topic = topic
    
    def consume(self):
        def reset_offset(consumer, partitions):
            if args.reset:
                for p in partitions:
                    p.offset = OFFSET_BEGINNING
                consumer.assign(partitions)

        # Subscribe to topic
        topic = "purchases"
        consumer.subscribe([topic], on_assign=reset_offset)
