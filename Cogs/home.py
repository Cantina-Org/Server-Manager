from flask import request, redirect, render_template, url_for


def home_cogs(database):
    if not request.cookies.get('token'):
        return redirect(url_for('login'))
    data = database.select('''SELECT user_name, admin FROM cantina_administration.user WHERE token = %s''',
                           (request.cookies.get('token'),), 1)
    try:
        return render_template('home.html', cur=data)
    except IndexError:
        return redirect(url_for('login'))
