from flask import redirect


def login_cogs(database):
    to_redirect = database.select('''SELECT fqdn FROM cantina_administration.domain WHERE name="cerbere"''', None,
                                  number_of_data=1)
    return redirect('https://'+to_redirect[0]+'/auth/server_manager', code=302)
