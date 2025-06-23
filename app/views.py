from app import app
from db.test import get_students_list, get_student_info
from flask import render_template, jsonify, request
import json

chat_id = 435680352

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def students():
    return render_template('students_list.html', title='Мои студенты')

@app.route('/profile')
def profile():
    user_id = request.args.get('user_id')
    # Здесь можно загрузить данные студента из базы данных
    return render_template('profile.html', user_id=user_id)

@app.route('/api/students', methods=['GET'])
def get_students():    
    # 1. поулчить chat_id из initDataUnsafe
    # 2. верифицировать hash

    try:
        students_list = get_students_list(chat_id)

        if not students_list:
            return "", 204

        return jsonify({
            "status": "success",
            "data": json.dumps(students_list)
        })

    except Exception as e:
        app.logger.error(f"Database error: {str(e)}")
        return jsonify({"status": "error", "message": "Database error"}), 500