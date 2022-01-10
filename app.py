from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from kafka import KafkaConsumer, KafkaProducer

from configparser import ConfigParser
from streams.streams import producer, consumer, confluent_producer, confluent_consumer

app = Flask(__name__)

config_parser = ConfigParser()
config_parser.read('getting_started.ini')
config = dict(config_parser['default'])

delta_producer: producer.Producer = confluent_producer.ConfluentProducer('deltas', config)

@app.route('/delta', methods=['POST'])
def uploadDelta():
    req = request.get_json()
    print(req)
    json_payload = json.dumps(req)
    json_payload = str.encode(json_payload)

    # delta_producer.produce('deltas', json_payload)
    print('Sent to consumer')
    return jsonify({
        "message": "The given sidewalk information will be entered into OSW",
        "status": "pass"
    })


@app.route('/delta-set', methods=['POST'])
def createSubgraph():
    req = request.get_json()
    print(req)
    json_payload = json.dumps(req)
    json_payload = str.encode(json_payload)

    delta_producer.produce(key='Austin', value=json_payload)
    print('Sent to consumer')
    return jsonify({
        "message": "The given sidewalk information will be entered into OSW",
        "status": "pass"
    })


@app.route('/test/sidewalks', methods=['POST'])
def testSidewalkProducer():
    req = request.get_json()
    print(req)
    json_payload = json.dumps(req)
    json_payload = str.encode(json_payload)

    producer.send('test-sidewalks', json_payload)
    producer.flush()
    print('Sent to consumer')
    return jsonify({
        "message": "The given sidewalk information will be entered into OSW",
        "status": "pass"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
