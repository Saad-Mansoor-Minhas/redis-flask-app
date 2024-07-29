from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/store', methods=['POST'])
def store_data():
    data = request.json.get('data')
    redis_client.set('key', data)
    return jsonify({"message": "Data stored successfully!"})

@app.route('/get', methods=['GET'])
def get_data():
    data = redis_client.get('key')
    return jsonify({"data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
