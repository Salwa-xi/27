from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import random
import time
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

patients = [
    {"id": 1, "name": "Salwa", "heart_rate": 0},
    {"id": 2, "name": "Jana", "heart_rate": 0},
    {"id": 3, "name": "Ali Ahmed", "heart_rate": 0},
]

@app.route('/')
def index():
    return render_template('index.html', patients=patients)

# API to return data
@app.route('/api/patients', methods=['GET'])
def get_patients():
    return jsonify(patients)

# push
def broadcast_heart_rates():
    while True:
        time.sleep(2)  # each 2 sec
        for patient in patients:
            patient['heart_rate'] = random.randint(60, 100)  # معدل نبضات عشوائي
        socketio.emit('update_data', patients)

thread = Thread(target=broadcast_heart_rates)
thread.start()

if __name__ == '__main__':
    socketio.run(app, debug=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
