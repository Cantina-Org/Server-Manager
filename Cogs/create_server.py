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

        mkdir(dir_path + secure_filename(request.form['server-name']))
        database.insert("""INSERT INTO cantina_server_manager.server(owner_token, server_name, server_token, 
        server_run_command, server_path, group_acces) VALUES (%s, %s, %s, %s, %s, %s)""",
                        (request.cookies.get("token"), request.form['server-name'], "0", request.form['server-cmd'],
                         dir_path + secure_filename(request.form['server-name']), 0))
        return redirect(url_for('server'))
