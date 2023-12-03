from datetime import datetime
from os import system
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename


def run_server_cogs(database, server_id):
    user_token = request.cookies.get('token')
    date = str(datetime.now())
    if not user_token:
        return redirect(url_for('login'))

    if server_id:
        data = database.select('SELECT server_run_command, server_path, name FROM cantina_server_manager.server '
                               'WHERE id=%s', (server_id,), 1)
        system('cd ' + data[1] + ' && ' + data[0] + ' > ' + data[1] + '/' + secure_filename(date + '-' + data[2]))
        return redirect(url_for('server', server_id=server_id))
