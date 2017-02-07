#!/usr/bin/env python
from bottle import Bottle, run, request, auth_basic

app = Bottle()


@app.route('/ua')
def ua():
    print(request.headers.get('User-Agent'))
    if request.headers.get('User-Agent') != 'python/requests':
        return "I don't like your browser, go away!"
    return "Hisss."


def check_auth(username, password):
    if username == 'admin' and password == '12308':
        return True
    return False


@app.route('/basic_auth')
@auth_basic(check_auth)
def basic():
    pass


if __name__ == "__main__":
    run(app, host='localhost', port=8017, reloader=True)
