from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# 1. GET végpont - Útvonal paraméter
@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    return jsonify({"message": f"Szia, {username}!"})

# 2. GET végpont - Lekérdezési paraméter
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    return jsonify({"message": f"Erre kerestél: {query}"})

# 3. GET végpont - Nincs paraméter
@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "A szerver fut"})

# 4. POST végpont - Kérés törzse (application/json)
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    return jsonify({"received": data})

# 5. POST végpont - Kérés törzse (űrlap adatok)
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    age = request.form.get('age')
    return jsonify({"name": name, "age": age})

# Süti beállítása
@app.route('/setcookie', methods=['GET'])
def set_cookie():
    resp = make_response(jsonify({"message": "Süti beállítva"}))
    resp.set_cookie('username', 'flaskuser')
    return resp

# Süti lekérése
@app.route('/getcookie', methods=['GET'])
def get_cookie():
    username = request.cookies.get('username')
    return jsonify({"cookie_value": username})

if __name__ == '__main__':
    app.run(debug=True)