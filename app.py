from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from kafka import KafkaConsumer, KafkaProducer

app = Flask(__name__)

TOPIC_NAME = "INFERENCE"
KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(
    bootstrap_servers = KAFKA_SERVER,
    api_version = (0, 11, 15)
)


@app.route('/delta', methods=['POST'])
def updateSidewalk():
    req = request.get_json()
    print(req)
    json_payload = json.dumps(req)
    json_payload = str.encode(json_payload)

    producer.send('deltas', json_payload)
    producer.flush()
    print('Sent to consumer')
    return jsonify({
        "message": "The given sidewalk information will be entered into OSW",
        "status": "pass"
    })


@app.route('/subgraph', methods=['POST'])
def createSubgraph():
    req = request.get_json()
    print(req)
    json_payload = json.dumps(req)
    json_payload = str.encode(json_payload)

    producer.send('subgraphs', json_payload)
    producer.flush()
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
