from flask import Flask, render_template
from flask_socketio import SocketIO
from flask import request
from spillebrett import Spillebrett
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

clients=[]
clientOrdbok={}
s = None

@app.route('/')
def sessions():
    return render_template('enkel.html')

@socketio.on('connect')
def connect():
    clients.append(request.sid)
    print("Client connected: " + request.sid)
    print(len(clients),"is connected")
    s.leggTilSpiller()

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected: ' + request.sid)
    clients.remove(request.sid)
    print(len(clients)," is connected")


#Alle motatte meldinger
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

@socketio.on('kommando')
def brukerKommando(json, methods=['GET', 'POST']):
    #print(json["user_name"], json["message"])
    s.sendKommando(json["user_name"], json["message"])


if __name__ == '__main__':
    s = Spillebrett(40, 60)
    socketio.run(app, debug=True)
