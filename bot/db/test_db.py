from connect import with_connection

@with_connection
def get_user(cur):
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    return result

print(get_user())