from flask import Flask, request

app = Flask(__name__)

@app.route('/your-api-endpoint', methods=['GET'])
def your_api_endpoint():
    username = request.args.get('username')
    password = request.args.get('password')
    # Tutaj dodaj logikę obsługi żądania
    return f'Hello, {username}! Password: {password}'

if __name__ == '__main__':
    app.run(debug=True)
