def make_log(database, action_name, user_ip, user_token, log_level, argument=None, content=None):
    if content:
        database.insert('''INSERT INTO cantina_administration.log(name, user_ip, user_token, argument, 
        log_level) VALUES (%s, %s, %s,%s,%s)''', (str(action_name), str(user_ip), str(content), argument, log_level))
    else:
        database.insert('''INSERT INTO cantina_administration.log(name, user_ip, user_token, argument, 
        log_level) VALUES (%s, %s, %s,%s,%s)''', (str(action_name), str(user_ip), str(user_token), argument, log_level))
