from flask import redirect, request, url_for, render_template


def show_server_cogs(database, server_id):
    user_token = request.cookies.get('token')
    if not user_token:
        return redirect(url_for('login'))

    if server_id:
        data = database.select('SELECT * FROM cantina_server_manager.server WHERE id=%s', (server_id,), 1)
        return render_template('server_data.html', data=data)
    else:
        data = database.select('SELECT * FROM cantina_server_manager.server', None)
        user_permission = database.select('SELECT admin FROM cantina_administration.user WHERE token=%s', (user_token,),
                                          1)
        return render_template('all_server.html', data=data, user_permission=user_permission)
