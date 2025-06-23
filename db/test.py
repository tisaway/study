import psycopg 
from psycopg.rows import dict_row
CONNECTION_URI='postgresql://study-tisaway.db-msk0.amvera.tech/study?user=postgres&password=hamster7'

# def with_auth(f):
#     def with_auth_(chat_id, *args, **kwargs):
#         with psycopg.connect(CONNECTION_URI) as conn:
#             with conn.cursor() as cur:
#                 user_id = cur.execute("SELECT user_id FROM users WHERE chat_id = %s", [chat_id]).fetchone()
#                 if not user_id:
#                     raise ValueError("User not found")
#                 else:
#                     user_id = user_id[0]
#             with conn.cursor(row_factory=dict_row) as cur:
#                 result = f(cur, user_id, *args, **kwargs)
#                 return result
#     return with_auth_

def with_dict(f):
    def with_dict_(get_dict, *args, **kwargs):
        row_factory = dict_row if get_dict else None
        return f(row_factory, *args, **kwargs)
    return with_dict_

def unwrap_first_result(f):
    def unwrap_first_result_(*args, **kwargs):
        result = f(*args, **kwargs)
        if result:
            return result[0]
        else:
            return result
    return unwrap_first_result_

@unwrap_first_result
def get_user_id(chat_id):
    with psycopg.connect(CONNECTION_URI) as conn:
        with conn.cursor() as cur:
            return cur.execute("SELECT user_id FROM users WHERE chat_id = %s", [chat_id]).fetchone()
        
# Поулчение информации о профиле по id чата с текущим пользователем
def get_user_by_chat_id(chat_id):
    with psycopg.connect(CONNECTION_URI) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            return cur.execute("SELECT first_name, last_name, fathers_name, phone_number, email, tg_username FROM users WHERE chat_id = %s", [chat_id]).fetchone()
        
# Поулчение информации о профиле по user_id
def get_user_by_user_id(user_id):
    with psycopg.connect(CONNECTION_URI) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            return cur.execute("SELECT first_name, last_name, fathers_name, phone_number, email, tg_username FROM users WHERE user_id = %s", [user_id]).fetcone()





# Для репетитора
def get_students_list(chat_id):
    teacher_id = get_user_id(chat_id)
    with psycopg.connect(CONNECTION_URI) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            return cur.execute("""SELECT u.user_id, u.first_name, u.last_name, u.fathers_name, ts.subject_info
                        FROM users u
                        JOIN teacher_student ts ON u.user_id = ts.student_id
                        WHERE ts.teacher_id = %s
                        ORDER BY u.first_name, u.last_name, u.fathers_name
                        """, [teacher_id]).fetchall()

def get_student_info(teacher_id, student_id):
    with psycopg.connect(CONNECTION_URI) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            return cur.execute("""SELECT u.*, ts.subject_info, ts.student_info
                        FROM users u
                        JOIN teacher_student ts ON u.user_id = ts.student_id
                        WHERE ts.teacher_id = %s AND u.user_id = %s
                        """, [teacher_id, student_id]).fetchall()
        
def get_parents_info(student_id):
    with psycopg.connect(CONNECTION_URI) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            return cur.execute("""SELECT u.*
                        FROM users u
                        JOIN parent_student ps ON u.user_id = ps.parent_id
                        WHERE ps.student_id = %s
                        """, [student_id]).fetchall()
        
def get_teacher_schedule(chat_id):
    teacher_id = get_user_id(chat_id)
    with psycopg.connect(CONNECTION_URI) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            return cur.execute("SELECT * FROM schedule WHERE teacher_id = %s", [teacher_id]).fetchall()
# @with_dict
# def get_student_full_info(student_id, row_factory=None):
#     with psycopg.connect(CONNECTION_URI) as conn:
#         with conn.cursor(row_factory=row_factory) as cur:
#             student_info = cur.execute("""
#                 SELECT u.first_name, u.last_name, u.father 
#                                        FROM users u
#                 WHERE u.user_id = %s
#             """, [student_id]).fetchone()

#             # Get parent info
#             parents = cur.execute("""
#                 SELECT u.user_id, u.first_name, u.last_name, u.fathers_name, u.phone_number, u.email
#                 FROM users u
#                 JOIN parent_student ps ON u.user_id = ps.parent_id
#                 WHERE ps.student_id = %s
#             """, [student_id]).fetchall()

#             return {
#                 'student': student_info,
#                 'grades': grades,
#                 'parents': parents
#             }

# kek = get_user_id(chat_id=435680352)
# kek = get_teacher_schedule(435680352)
# print(kek)