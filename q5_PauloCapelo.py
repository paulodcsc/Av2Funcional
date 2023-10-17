from flask import Flask, request, jsonify

#QUESTÃO 2 ADAPTADA PARA QUESTÃO 5 USANDO FLASK

app = Flask(__name)

def register_user(username, password):
    with open('users.txt', 'a') as file:
        file.write(f'{username} {password}\n')

def login_user(username, password):
    with open('users.txt', 'r') as file:
        for line in file:
            if line.strip() == f'{username} {password}':
                return 'SUCCESS'
    return 'FAILURE'

@app.route('/register', methods=['POST'])
def handle_register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    register_user(username, password)
    return jsonify({'message': 'User registered successfully!'})

@app.route('/login', methods=['POST'])
def handle_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    result = login_user(username, password)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
