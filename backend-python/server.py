from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/disclosed-attributes', defaults={'path': ''}, methods=['GET'])
@app.route('/api/disclosed-attributes/<path:path>', methods=['GET'])
def disclosed_attributes(path):
    api_key = '4edafd47a67584c563d6fc3f4d105d2900062c57352ec3db2dc1c962b57dce2e'
    
    try:
        # Construct the target URL
        target_path = f'/api/disclosed-attributes/{path}' if path else '/api/disclosed-attributes'
        target_url = f'https://wallet-connect.eu{target_path}'
        
        response = requests.get(
            target_url,
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            },
            params=request.args,
            verify=False  # Disable SSL verification due to Python venv SSL config issue. Do not use in production
        )
        
        return jsonify(response.json()), response.status_code
        
    except Exception as e:
        print(f"Request error: {e}")
        return jsonify({'error': 'Proxy error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(port=4000)
    print('Backend running on port 4000')