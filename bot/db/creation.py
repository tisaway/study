from connect import with_connection

@with_connection
def create_db(cur):
    cur.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        -- user_id - id чата с пользователем
                        user_id BIGINT PRIMARY KEY,
                        tg_username TEXT UNIQUE,
                        first_name TEXT NOT NULL,
                        father_name TEXT,
                        last_name TEXT NOT NULL,
                        phone_number TEXT,
                        email TEXT
                    );

                    CREATE TABLE IF NOT EXISTS parent_student (
                        parent_id BIGINT REFERENCES users(user_id),
                        student_id BIGINT REFERENCES users(user_id),
                        PRIMARY KEY (parent_id, student_id)
                    );

                    CREATE TABLE IF NOT EXISTS teacher_student (
                        teacher_id BIGINT REFERENCES users(user_id),
                        student_id BIGINT REFERENCES users(user_id),
                        PRIMARY KEY (teacher_id, student_id)
                    );

                    -- tasks
                    CREATE TABLE IF NOT EXISTS tasks (
                        task_id SERIAL PRIMARY KEY,
                        teacher_id BIGINT REFERENCES users(user_id),
                        title TEXT NOT NULL,
                        description TEXT,
                        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                        deadline TIMESTAMP WITH TIME ZONE
                    );

                    -- task targets (individual students or future groups)
                    CREATE TABLE IF NOT EXISTS task_targets (
                        task_id INT REFERENCES tasks(task_id),
                        student_id BIGINT REFERENCES users(user_id),
                        PRIMARY KEY (task_id, student_id)
                    );

                    -- Student submissions
                    CREATE TABLE IF NOT EXISTS submissions (
                        submission_id SERIAL PRIMARY KEY,
                        task_id INT REFERENCES tasks(task_id),
                        student_id BIGINT REFERENCES students(student_id),
                        content TEXT,
                        submitted_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                        status TEXT DEFAULT 'submitted' CHECK (status IN ('submitted', 'graded'))
                    );

                    -- Grades and feedback
                    CREATE TABLE IF NOT EXISTS grades (
                        grade_id SERIAL PRIMARY KEY,
                        submission_id INT REFERENCES submissions(submission_id),
                        teacher_id BIGINT REFERENCES teachers(teacher_id),
                        score NUMERIC(3, 2),
                        feedback TEXT,
                        graded_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
                    );

                    -- Schedule
                    CREATE TABLE IF NOT EXISTS schedule (
                        lesson_id SERIAL PRIMARY KEY,
                        teacher_id BIGINT REFERENCES teachers(teacher_id),
                        student_id BIGINT REFERENCES students(student_id),
                        lesson_time TIMESTAMP WITH TIME ZONE NOT NULL,
                        duration INTERVAL NOT NULL,
                        topic TEXT,
                        status TEXT DEFAULT 'planned' CHECK (status IN ('planned', 'completed', 'canceled'))
                    );

                    -- Notifications
                    CREATE TABLE IF NOT EXISTS notifications (
                        notification_id SERIAL PRIMARY KEY,
                        user_id BIGINT REFERENCES users(user_id),
                        message TEXT NOT NULL,
                        sent_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                        is_read BOOLEAN DEFAULT FALSE
                    );
                    ''')

create_db()    