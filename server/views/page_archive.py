from flask import request, jsonify, send_from_directory
from app import app
from tools.cors import response
from tools import sql


@app.route('/archive/get_tasks', methods=['GET'])
def get_tasks_a():
    tasks = sql.get_archive_tasks()
    return response({'data': tasks})
