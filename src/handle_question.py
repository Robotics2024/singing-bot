from flask import Flask, request, jsonify
from flask_cors import CORS
from asking_question import asking_question

app = Flask(__name__)
CORS(app, resources={r"/test": {"origins": "http://localhost:8000"}})  # Enable CORS for /test route
CORS(app, resources={r"/handle_question": {"origins": "*"}}) 

@app.route('/handle_question', methods=['POST'])
def handle_question():
    data = request.get_json()
    print(data)
    response = asking_question(data['question'])

    return jsonify({'answer': response})

@app.route('/test', methods=['GET'])
def test_endpoint():
    response = "here your answer"
    return jsonify({'answer': response})

if __name__ == '__main__':
    app.run(debug=True, port=8000)