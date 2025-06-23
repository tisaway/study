# import psycopg2 
# import psycopg2.extras
# from config import DB_NAME, DB_HOST, DB_USER, DB_PASS, DB_PORT

# def with_connection(f):
#     def with_connection_(*args, **kwargs):
#         conn = psycopg2.connect(dbname=DB_NAME, host=DB_HOST, user=DB_USER, password=DB_PASS, port=DB_PORT)
#         cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
#         result = f(cur, *args, **kwargs)
#         conn.commit()
#         conn.close()
#         return result
#     return with_connection_

import psycopg
from config import CONNECTION_URI



def with_connection(f):
    def with_connection_(*args, **kwargs):
        with psycopg.connect(CONNECTION_URI) as conn:
            with conn.cursor() as cur:
                result = f(cur, *args, **kwargs)
                # conn.commit()
                return result
    return with_connection_