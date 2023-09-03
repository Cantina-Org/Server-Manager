from datetime import datetime

from flask import request, redirect, url_for


def run_server_cogs(database, server_id):
    user_token = request.cookies.get('token')
    date = str(datetime.now())
    if not user_token:
        return redirect(url_for('login'))

    if server_id:
        data = database.select('SELECT run_command, path, name FROM cantina_server_manager.server WHERE id=%s',
                               (server_id,), 1)
        # system('cd ' + data[1] + ' && ' + data[0] + ' > ' + log_path + secure_filename(date + '-' + data[2]))
        return redirect(url_for('server', server_id=server_id))
