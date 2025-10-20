from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('ele.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():  # Renamed the function to 'predict' to avoid endpoint function overwriting
    data1 = request.form['Day']
    data2 = request.form['Month']
    data3 = request.form['SystemLoadEA']
    data4 = request.form['SMPEA']
    data5 = request.form['ORKTemperature']
    data6 = request.form['ORKWindspeed']
    data7 = request.form['CO2Intensity']
    data8 = request.form['ActualWindProduction']
    data9 = request.form['ForecastWindProduction']
    data10 = request.form['SystemLoadEP2']
    arr = np.array([[data1, data2, data3, data4,data5,data6,data7,data8,data9,data10]])
    pred = model.predict(arr)
    return render_template('result.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)
