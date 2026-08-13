import json
import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, 
            static_folder='assets', 
            static_url_path='/assets',
            template_folder='')

@app.route('/')
def index():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            info = json.load(f)
    except FileNotFoundError:
        info = {}
    return render_template('index.html', data=info)

@app.route('/data.json')
def serve_json():
    return send_from_directory(os.getcwd(), 'data.json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)