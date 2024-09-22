from api.module import gpt_answer, bing_image_answer
from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

@app.route('/static/<path:filename>')
def serve_static(filename):
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    return send_from_directory(static_dir, filename)

def handle_request(message, response_function):
    if not message:
        return jsonify({'error': 'No messages provided'}), 400

    response_text = "(Powered by OpenFXT): "
    try:
        response = response_function(message)
        response_text += response
    except Exception as e:
        response_text += str(e)

    return jsonify({'text': response_text}), 200

@app.route('/api/v2/simple_response', methods=['POST'])
def process_messages_simple():
    data = request.json
    message = ("Reply simply and concisely, add some icons to make the response more lively. "
               "Always use Vietnamese to respond, and if someone asks who you are, reply that you are ChatFXT, "
               "a chatbot response service API built and maintained by OpenFXT. " + data.get('message', ''))
    return handle_request(message, gpt_answer)

@app.route('/api/v2/detail_response', methods=['POST'])
def process_messages_detail():
    data = request.json
    message = ("Let adding some icons to make the response more lively. Always use Vietnamese to respond, "
               "and if someone asks who you are, reply that you are ChatFXT, a chatbot response service API built "
               "and maintained by OpenFXT. " + data.get('message', ''))
    return handle_request(message, gpt_answer)

@app.route('/api/v2/image_response', methods=['POST'])
def process_messages_image():
    data = request.json
    message = data.get('message', '')
    return handle_request(message, bing_image_answer)

if __name__ == '__main__':
    app.run(debug=True)
