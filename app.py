from unittest import result
import numpy as np
from flask import Flask, request, jsonify, render_template
from  ocr_license_plate import get_number

app = Flask(__name__)

@app.route('/', methods =['Get'])
def home():
    result = ""
    return render_template('index.html')

# @app.route('/')
# def get_home():
#     result = ""
#     return render_template('index.html')

@app.route('/getnumber', methods =['Post'])
def getnumber():
    """
        For rendering results in index.html GUI
    """
    path = request.form['path']
    result = get_number(path)

    return render_template('index.html', prediction_text = "Numplate is : {}".format(result))

if __name__ == "__main__":
    app.run(debug=True)
    
