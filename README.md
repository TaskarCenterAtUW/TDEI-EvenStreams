# TDEI-EvenStreams
Transportation Data Equity Initiative event streams infrastructure

## How to Start the event streams

1. Navigate to the Kafka directory (kafka_2.13-3.0.0)
2. Start the Zookeeper service with the following command: `bin/zookeeper-server-start.sh config/zookeeper.properties`
3. Start the Kafka broker service with the following command: `bin/kafka-server-start.sh config/server.properties`
4. Now that the Kafka streams are running, you can start the event streaming application. Navigate to the TDEI-EventStreams directory and run the following:
    - `source env/bin/activate`
    - `python subgraph_consumer.py`
    - `python delta_consumer.py`
    - `python app.py`