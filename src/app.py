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

@app.route('/<string: country>/<string: variety>/<float: aroma>/<float: aftertaste>/<float: acidity>/<float: body>/<float: balance>/<float: moisture>')
def result(country, variety, aroma, aftertaste, acidity, body, balance, moisture):
    cols = ['country_of_origin', 'variety', 'aroma', 'aftertaste', 'acidity', 'body', 'balance', 'moisture']
    data = [country, variety, aroma, aftertaste, acidity, body, balance, moisture]
    posted = pd.DataFrame(np.array(data).reshape(1,8), columns=cols)
    loaded_model = pickle.load(open('../models/coffee_model.pkl', 'rb')) #rb es read binary
    result = loaded_model.predict(posted)
    text_result = result.tolist()[0]
    if text_result == 'Yes':
        return jsonify(message = 'Your coffee is great!'), 200
    else:
        return jsonify(message = 'Your coffee sucks!'), 200

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

