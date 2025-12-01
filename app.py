
import os
from flask import Flask, jsonify, request
app = Flask(__name__)

try:
    
    import api as user_api
    
    if hasattr(user_api, 'app'):
        app = user_api.app
except Exception:
    pass

@app.route('/health')
def health():
    return jsonify({'status':'ok'})

@app.route('/example-analytics', methods=['POST'])
def example_analytics():
    
    data = request.get_json(force=True, silent=True) or {}
    
    score = len(str(data)) % 10
    return jsonify({'received': data, 'score': score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
