#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count(parameter):
    for i in range(int(parameter)):
        print(i)
    return '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(int(num1) + int(num2))
    if operation == '-':
        return str(int(num1) - int(num2))
    if operation == '*':
        return str(int(num1) * int(num2))
    if operation == 'div':
        return str(int(num1) / int(num2))
    if operation == '%':
        return str(int(num1) % int(num2))
    
    return 'Invalid operation'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
