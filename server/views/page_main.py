from flask import request, jsonify, send_from_directory
from app import app
from tools.cors import response
from tools import sql


@app.route('/main/get_tasks', methods=['GET'])
def get_tasks_m():
    tasks = sql.get_main_tasks()
    return response({'data': tasks})
