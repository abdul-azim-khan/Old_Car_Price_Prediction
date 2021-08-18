import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("rf.pickle","rb"))




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # 'mileage', 'tax', 'mpg', 'engineSize', 'age', 'transmission_Automatic',
    #    'transmission_Manual', 'transmission_Semi-Auto', 'fuelType_Diesel',
    #    'fuelType_Hybrid', 'fuelType_Other', 'fuelType_Petrol'

    transmission_Automatic =0
    transmission_Manual = 0
    transmission_SemiAuto =0

    fuelType_Diesel=0
    fuelType_Hybrid =0
    fuelType_Other =0
    fuelType_Petrol =0

    if request.method == "POST":
        age = int(request.form["age"])
        mileage = int(request.form["run"])
        tax = int(request.form["tax"])
        mpg = int(request.form["mpg"])
        engineSize = int(request.form["eng_size"])

        transmission = request.form["transmission"]
        if (transmission == "automatic"):
            transmission_Automatic =1
            transmission_Manual = 0
            transmission_SemiAuto =0
        
        elif (transmission == "manual"):
            transmission_Automatic =0
            transmission_Manual = 1
            transmission_SemiAuto =0

        elif (transmission == "semi-auto"):
            transmission_Automatic =0
            transmission_Manual = 0
            transmission_SemiAuto =1
    
        fuelType = request.form["fuelType"]
        if (fuelType == 'diesel'):
            fuelType_Diesel=1
            fuelType_Hybrid =0
            fuelType_Other =0
            fuelType_Petrol =0

        elif (fuelType == 'hybrid'):
            fuelType_Diesel=0
            fuelType_Hybrid =1
            fuelType_Other =0
            fuelType_Petrol =0
        
        elif (fuelType == 'other'):
            fuelType_Diesel=0
            fuelType_Hybrid =0
            fuelType_Other =1
            fuelType_Petrol =0

        elif (fuelType == 'petrol'):
            fuelType_Diesel=0
            fuelType_Hybrid =0
            fuelType_Other =0
            fuelType_Petrol =1
        

    

        pred = model.predict([[mileage, tax, mpg, engineSize, age, transmission_Automatic,transmission_Manual, transmission_SemiAuto, fuelType_Diesel,fuelType_Hybrid, fuelType_Other, fuelType_Petrol ]])
        output= round(pred[0])
        
        return render_template("index.html",prediction_text="You can sell this car at {} $".format(output))

    #     if output<0:
    #         return render_template("index.html", prediction_text="Sorry your car can't be sold")
    #     else:
    #         return render_template("index.html",prediction_text="You can sell this car at {} Rs".format(output))
    #         print("Sell car at {}".format(output))    
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)






    
