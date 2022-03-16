from flask import request, jsonify, send_from_directory
from app import app
from tools.cors import response
from tools import sql


@app.route('/')
def hello_world():
    sql.db.create_all()
    return 'Hello, world!'


@app.route('/add_answer', methods=['POST'])
def add_answer():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    answer = request.form.get('answer')
    task_id = request.form.get('task_id')
    data = {'status': False, 'warn': 'строки не должны быть пустыми'}
    if first_name and last_name and answer and task_id:
        try:
            sql.add_new_answer(first_name, last_name, answer, task_id)
            data = {'status': True}
        except Exception as ex:
            print(ex)
            data = {'status': False, 'warn': "Ответ не был добавлен в бд"}
    return response(data)


@app.route('/add_request', methods=['POST'])
def add_task_req():
    title = request.form.get('title')
    description = request.form.get('description')
    start_code = request.form.get('start_code')
    comment = request.form.get('comment')
    data = {'status': False, 'warn': 'Заполните обязательные строки'}
    if title and description:
        try:
            sql.add_new_task_request(title, description, start_code, comment)
            data = {'status': True}
        except Exception as ex:
            print(ex)
            data = {'status': False, 'warn': "Ответ не был добавлен в бд"}
    return response(data)


@app.route('/get_answer', methods=['GET'])
def get_answer():
    answer_id = request.args.get('id')
    return response(sql.get_answer_by_id(answer_id))

