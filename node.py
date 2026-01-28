from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

# Each node has its own local storage
storage = {}

@app.route('/put', methods=['PUT'])
def put_value():
    data = request.json
    key = data.get("key")
    value = data.get("value")

    if not key:
        return jsonify({"error": "Key is required"}), 400

    storage[key] = value
    return jsonify({"status": "stored", "key": key, "value": value})


@app.route('/get', methods=['GET'])
def get_value():
    key = request.args.get("key")

    if key in storage:
        return jsonify({"key": key, "value": storage[key]})
    else:
        return jsonify({"error": "Key not found"}), 404


if __name__ == '__main__':
    port = int(sys.argv[1])
    app.run(port=port)
