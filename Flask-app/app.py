from flask import Flask, request, render_template, jsonify
from gradio_client import Client

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    input_text = data.get('text', '')
    client = Client('Sajjad43/app-multi-label-classification-imdb')
    result = client.predict(context=input_text, api_name='/predict')
    #if isinstance(result, list):
        #result = ', '.join(result)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
    

