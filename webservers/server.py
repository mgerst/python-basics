#!/usr/bin/env python
from bottle import Bottle, run, request, auth_basic, response, abort
import json

app = Bottle()


@app.route('/ua')
def ua():
    print(request.headers.get('User-Agent'))
    if request.headers.get('User-Agent') != 'python-scraper/1.0':
        return "I don't like your browser, go away!"
    return "Hisss."


def check_auth(username, password):
    if username == 'admin' and password == '308':
        return True
    return False


@app.route('/basic_auth')
@auth_basic(check_auth)
def basic():
    return "Welcome authenticated user!"


@app.route('/token')
def token():
    auth = request.get_header('Authorization')
    if auth:
        method, value = auth.split(' ')

        if method == "Token" and value == "142":
            return "Success!"

    abort(401, "Unauthorized")


@app.route('/set_cookie')
def set_cookie():
    response.set_cookie("authenticated", "yes")


@app.route('/cookie')
def cook():
    if request.get_cookie("authenticated") == "yes":
        return "You are a valid user"
    else:
        abort(401, "Access denied")


@app.route('/json')
def json_data():
    if request.get_cookie("authenticated") == "yes":
        return json.dumps({"error": False})
    else:
        return json.dumps({"error": True, "message": "You are not authorized"})


if __name__ == "__main__":
    run(app, host='localhost', port=8017, reloader=True)
