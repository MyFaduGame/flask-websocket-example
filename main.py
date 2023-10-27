from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key
socketio = SocketIO(app)

@app.route('/')
def index():
    return {'date':"Hello World"}  # You can create an HTML template for your web page

@socketio.on('message')
def handle_message(message):
    print(f'Received message: {message}')
    socketio.emit('response', message)  # Send the message back to the client

if __name__ == '__main__':
    socketio.run(app, debug=True)
