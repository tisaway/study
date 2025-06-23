CREATE TABLE users (
    user_id INT PRIMARY KEY,
    tg_username TEXT UNIQUE,
    chat_id TEXT UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT,
    email TEXT
);

CREATE TABLE parent_student (
    parent_student_id INT PRIMARY KEY,
    parent_id INT,
    student_id INT
);
CREATE TABLE teacher_student (
    teacher_student_id INT PRIMARY KEY,
    teacher_id INT,
    student_id INT,
    student_info TEXT
);
-
CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    teacher_student_id INT NOT NULL,
    message_id TEXT NOT NULL,
    title TEXT NOT NULL,
    created_at TEXT  NOT NULL,
    deadline TEXT NOT NULL,
    status TEXT  NOT NULL
);

-- Student submissions
CREATE TABLE submissions (
    submission_id SERIAL PRIMARY KEY,
    task_id INT,
    message_id TEXT NOT NULL,
    submitted_at TIMESTAMP NOT NULL
);
-- Grades and feedback
CREATE TABLE grades (
    grade_id SERIAL PRIMARY KEY,
    task_id INT,
    grade INT NOT NULL,
    feedback TEXT,
    graded_at TIMESTAMP NOT NULL
);
-- Schedule
CREATE TABLE schedule (
    lesson_id SERIAL PRIMARY KEY,
    teacher_student_id INT NOT NULL,
    start_time TIMESTAMP NOT NULL,
    duration_min INT NOT NULL,
  	reminder_min INT NOT NULL,
  	interval_days INT NOT NULL
);
