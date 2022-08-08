from flask import Flask, render_template, jsonify, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_flask(): 
    return 'Hello flask'

@app.route('/inicio') #renderiza página web
def show_home():
    return render_template('index.html')

@app.route('/url_variables/<string: name>/<int: age>')
def url_variables(name, age):
    if age < 18: 
        return jsonify(message = 'Lo siento' + name + 'no estás autorizado'), 401
    else:
        return jsonify(message = 'Bienvenido' + name), 200

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

