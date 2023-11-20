from flask import jsonify

def success(data, success, status):
    return jsonify({
        "data": data,
        "success": success,
    }), status

def error(message, status):
    return jsonify({
        "error": message,
        "success": False,
    }), status
