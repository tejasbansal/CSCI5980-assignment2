from flask import Flask, request, jsonify
import json
import datetime
import threading

app = Flask(__name__)

data_file = "data.json"
log_file = "dataLog.json"

def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def log_request(request_type, key):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = {
        "timestamp": timestamp,
        "request_type": request_type,
        "key": key
    }
    with open('dataLog.json', 'a') as log_file:
        json.dump(log_entry, log_file)
        log_file.write('\n')

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file)

kv_store = load_data()

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"

@app.route('/get/<key>', methods=['GET'])
def get_value(key):
    if key in kv_store:
        log_request('GET', key)
        return str(kv_store[key]), 200
    else:
        log_request(f"Key '{key}' not found")
        return "Key not found\n", 404

@app.route('/put', methods=['PUT'])
def put_value():
    key = request.args.get('key')
    value = request.args.get('value')
    if key and value:
        kv_store[key] = value
        print("h",kv_store)
        save_data(kv_store)
        log_request('PUT', key)
        return jsonify("Value set successfully"), 200
    else:
        log_request(f"Key '{key}' Invalid data format")
        return jsonify("Invalid data format"), 400


@app.route('/set/<key>', methods=['DELETE'])
def del_value(key):
    if key in kv_store:
        del kv_store[key]
        save_data(kv_store)
        log_request('DELETE', key)
        return "Deleted successfully\n",200
    else:
        log_request(f"Key '{key}' Invalid data format")
        return "Key not found\n", 404
    
def run_server():
    app.run(threaded=True, host='127.0.0.1', port=5000)

if __name__ == '__main__':
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

