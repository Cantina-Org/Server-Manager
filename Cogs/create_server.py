from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from os import mkdir
from pymysql.err import OperationalError


def create_server_cogs(database, alert, dir_path):
    user_token = request.cookies.get('token')
    if not user_token:
        return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template('create_server.html', alert=alert)
    elif request.method == 'POST':
        if not request.form['server-name'] or not request.form['server-cmd']:
            return redirect(url_for('create_server', alert='field-empy'))

        try:
            mkdir(dir_path + secure_filename(request.form['server-name']))
            database.insert("""INSERT INTO cantina_server_manager.server(name, local_name, owner_name, permission) 
            VALUES (%s, %s, %s, %s)""", (request.form['server-name'], '', '', {}))
            return redirect(url_for('server'))
        except FileExistsError as e:
            print(e)
            return redirect(url_for('create_server', alert='file-existe'))
        except OperationalError as e:
            print(e)
            return redirect(url_for('create_server', alert='db-prob'))
