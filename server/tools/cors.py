from flask import jsonify


def response(data: dict):
    resp = jsonify(data)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp
