import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

#Load pickel file
filename = 'student_pred_model.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        hour = float(request.form['study_hours'])

        reusult = model.predict([[hour]])[0].round(2)

        return render_template('index.html',pred_result = reusult,hour_syudy=hour)






if __name__ == "__main__":
    app.run(debug=True)