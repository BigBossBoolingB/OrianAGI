from flask import Flask, render_template, jsonify, request
import json
import os
from .core import OrianAGI

app = Flask(__name__)

# Load model
config_path = os.path.join(os.path.dirname(__file__), '..', 'system_config.json')
with open(config_path, 'r') as f:
    config = json.load(f)
model = OrianAGI.from_json(config)

@app.route('/')
def index():
    return render_template('index.html', model=model)

@app.route('/api/status')
def status():
    return jsonify(model.status_report())

@app.route('/api/nodes')
def nodes():
    nodes_data = [
        {"id": n.id, "name": n.name, "status": n.status, "load": n.extra_data.get('load', 'N/A')}
        for n in model.node_manager.nodes
    ]
    return jsonify(nodes_data)

@app.route('/api/poetic', methods=['POST'])
def poetic():
    theme = request.json.get('theme', 'Quantum')
    poem = model.poetic_engine.generate_poem(theme)
    return jsonify({"poem": poem})

@app.route('/api/train', methods=['POST'])
def train():
    dataset = request.json.get('dataset', 'standard')
    model.train(dataset)
    return jsonify({"status": "Training initiated"})

@app.route('/api/reason', methods=['POST'])
def reason():
    query = request.json.get('query', '')
    res = model.reasoning.synthesize_reasoning(query)
    return jsonify(res)

@app.route('/api/qmoe', methods=['POST'])
def qmoe():
    res = model.qmoe.route(None)
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
