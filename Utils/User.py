def find_user_name(cursor, user_token):
    data = cursor.select("""SELECT user_name FROM cantina_administration.user WHERE token=%s""", (user_token,), 1)
    return data[0]


def is_user_admin(cursor, user_token):
    data = cursor.select("""SELECT admin FROM cantina_administration.user WHERE token=%s""", (user_token,), 1)
    return data[0]
