from flask import Flask, request, redirect, url_for
from Utils import Database
from datetime import datetime
from os import getcwd, path
from json import load

from Cogs.login import login_cogs
from Cogs.home import home_cogs
from Cogs.show_server import show_server_cogs
from Cogs.create_server import create_server_cogs

dir_path = path.abspath(getcwd()) + '/server/'
app = Flask(__name__)
with open(path.abspath(getcwd()) + "/config.json") as conf_file:
    config_data = load(conf_file)

database = Database.DataBase(user=config_data['database'][0]['database_username'],
                             password=config_data['database'][0]['database_password'],
                             host="localhost", port=3306)
database.connection()


@app.route('/')
def home():
    return home_cogs(database)


@app.route('/login', methods=['POST', 'GET'])
def login():
    return login_cogs(database)


@app.route('/server/<server_id>')
@app.route('/server')
def server(server_id=None):
    return show_server_cogs(database, server_id)


@app.route('/server/<server_id>/run')
def run_server(server_id=None):
    user_token = request.cookies.get('token')
    date = str(datetime.now())
    if not user_token:
        return redirect(url_for('login'))

    if server_id:
        data = database.select('SELECT run_command, path, name FROM cantina_server_manager.server WHERE id=%s',
                               (server_id,), 1)
        # system('cd ' + data[1] + ' && ' + data[0] + ' > ' + log_path + secure_filename(date + '-' + data[2]))
        return redirect(url_for('server', server_id=server_id))


@app.route('/server/create', methods=['POST', 'GET'])
def create_server(alert=False):
    return create_server_cogs(database, alert, dir_path)


if __name__ == '__main__':
    app.run(port=config_data["port"])
