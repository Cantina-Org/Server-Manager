from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from Utils import Database
from datetime import datetime
from os import getcwd, path, mkdir, system
from json import load

from Cogs.login import login_cogs
from Cogs.home import home_cogs

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
    user_token = request.cookies.get('token')
    if not user_token:
        return redirect(url_for('login'))

    if server_id:
        data = database.select('SELECT * FROM cantina_server_manager.server WHERE id=%s', (server_id,), 1)
        return render_template('server_data.html', data=data)
    else:
        data = database.select('SELECT * FROM cantina_server_manager.server')
        user_permission = database.select('SELECT admin FROM cantina_administration.user WHERE token=%s', (user_token,),
                                          1)
        return render_template('all_server.html', data=data, user_permission=user_permission)


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
    user_token = request.cookies.get('token')
    if not user_token:
        return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template('create_server.html', alert=alert)
    elif request.method == 'POST':
        if not request.form['server-name'] or not request.form['server-cmd']:
            return redirect(url_for('create_server', alert=True))

        server_name = request.form['server-name']
        server_cmd = request.form['server-cmd']
        server_path = dir_path+secure_filename(server_name)

        mkdir(server_path)
        database.insert("""INSERT INTO cantina_server_manager.server(server_name, owner_token, server_run_command,
         server_path) VALUES (%s, %s, %s, %s)""", (server_name, request.cookies.get('token'), server_cmd,
                                                   server_path))
        return redirect(url_for('server'))


if __name__ == '__main__':
    app.run(port=config_data["port"])
