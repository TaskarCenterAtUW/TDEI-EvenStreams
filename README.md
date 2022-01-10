# TDEI-EvenStreams
Transportation Data Equity Initiative event streams infrastructure

## How to Start the event streams

1. If not already running, start the Kafka cluster by starting the Docker container located in the root directory, using the following command: `docker-compose up -d`
2. Start the Python environment by running in the root directory: `source env/bin/activate`
3. Run app.py with `python app.py` in the Python environment. This will start the API server so it can start listening for requests.
4. To send a request to the `/delta-set` endpoint, you can try running the following curl request (The streams are currently not in production, so we can send anything to them. Eventually we should separate these, however.): `curl --header "Content-Type: application/json" -d @./Austin_Ways.geojson http://127.0.0.1:5000/delta-set`

TODO: Add the API gateway so it routes requests the event streams API.

## Creating a topic
```
docker-compose exec broker kafka-topics --create --topic deltas --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```