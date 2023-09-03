from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from os import mkdir


def create_server_cogs(database, alert, dir_path):
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
        server_path = dir_path + secure_filename(server_name)

        mkdir(server_path)
        database.insert("""INSERT INTO cantina_server_manager.server(server_name, owner_token, server_run_command,
             server_path) VALUES (%s, %s, %s, %s)""", (server_name, request.cookies.get('token'), server_cmd,
                                                       server_path))
        return redirect(url_for('server'))
