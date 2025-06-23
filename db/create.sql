CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    -- ФИО
    first_name TEXT NOT NULL,
    last_name TEXT,
    fathers_name TEXT,
    -- Контактная информация
    phone_number TEXT UNIQUE,
    email TEXT UNIQUE,
    tg_username TEXT UNIQUE,
    -- Если пользователь зарегистрирован в боте
    chat_id INT UNIQUE
);

CREATE TABLE IF NOT EXISTS teacher_student (
    teacher_student_id SERIAL PRIMARY KEY,
    
    teacher_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    student_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    -- Дополнительная информация
    subject_info TEXT,
    student_info TEXT
);

CREATE TABLE IF NOT EXISTS parent_student (
    parent_student_id SERIAL PRIMARY KEY,

    student_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    parent_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tasks (
    task_id SERIAL PRIMARY KEY,
    
    title TEXT NOT NULL,
    message_id TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS assigned_tasks (
    assignment_id SERIAL PRIMARY KEY,

    task_id INT NOT NULL REFERENCES tasks(task_id) ON DELETE CASCADE,
    teacher_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    student_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,

    deadline TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS submissions (
    submission_id SERIAL PRIMARY KEY,

    assignment_id INT REFERENCES assigned_tasks(assignment_id),
    message_id TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS grades (
    grade_id SERIAL PRIMARY KEY,
    
    assignment_id INT REFERENCES assigned_tasks(assignment_id),
    grade INT NOT NULL,
    feedback TEXT,
    graded_at TIMESTAMP NOT NULL
);


CREATE TABLE IF NOT EXISTS schedule (
    lesson_id SERIAL PRIMARY KEY,

    teacher_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    student_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,

    start_time TIMESTAMP NOT NULL,
    duration_min INT NOT NULL,
    interval_days INT NOT NULL DEFAULT 0
);