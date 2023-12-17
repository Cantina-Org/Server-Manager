from flask import Flask
from os import getcwd, path
from json import load
from cantinaUtils.Database import DataBase
from flask_sock import Sock
from Cogs.login import login_cogs
from Cogs.home import home_cogs
from Cogs.show_server import show_server_cogs
from Cogs.create_server import create_server_cogs

dir_path = path.abspath(getcwd()) + '/server/'
app = Flask(__name__)
sock = Sock(app)
with open(path.abspath(getcwd()) + "/config.json") as conf_file:
    config_data = load(conf_file)

database = DataBase(user=config_data['database'][0]['database_username'],
                    password=config_data['database'][0]['database_password'], host="localhost", port=3306)
database.connection()


@app.route('/')
def home():
    return home_cogs(database)


@app.route('/login', methods=['POST', 'GET'])
def login():
    return login_cogs(database)


@app.route('/server/<server_id>')
@app.route('/server/')
@app.route('/server')
def server(server_id=None):
    return show_server_cogs(database, server_id)


@sock.route('/server/ws')
def run_server(socket):
    while True:
        data = socket.receive()
        socket.send(data)


@app.route('/server/create', methods=['POST', 'GET'])
def create_server(alert=False):
    return create_server_cogs(database, alert, dir_path)


if __name__ == '__main__':
    app.run(port=config_data["port"])
