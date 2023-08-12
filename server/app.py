#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>') 
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    count = f''
    for num in range(parameter):
        count += f'{num}\n'
    return count

@app.route('/math/<int:parameter>/<string:operation>/<int:parameter2>')
def math(parameter, operation, parameter2):
    if operation == "div":
        return str(parameter / parameter2)
    elif operation == "+":
        return str(parameter + parameter2)
    elif operation == "-":
        return str(parameter - parameter2)
    elif operation == "*":
        return str(parameter * parameter2)
    elif operation == "%":
        return str(parameter % parameter2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)