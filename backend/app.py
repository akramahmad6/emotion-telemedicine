from flask import Flask, request, jsonify
from flask_cors import CORS
from sentiment import analyze_emotion
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

app = Flask(__name__)
CORS(app)

cred = credentials.Certificate('../serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://emotion-telemedicine-default-rtdb.firebaseio.com'
})

@app.route('/')
def home():
    return jsonify({'status': 'EmoCare Backend Running!'})

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    message = data.get('message', '')
    patient_id = data.get('patientId', 'unknown')

    if not message:
        return jsonify({'error': 'No message provided'}), 400

    result = analyze_emotion(message)

    ref = db.reference('messages')
    ref.push({
        'message': message,
        'emotion': result['emotion'],
        'confidence': result['confidence'],
        'patientId': patient_id,
        'timestamp': datetime.now().isoformat()
    })

    return jsonify({
        'emotion': result['emotion'],
        'confidence': result['confidence'],
        'message': message
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)