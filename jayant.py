from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd

model=pickle.load(open("model.pkl","rb"))

#app object created for flask named app
app=Flask(__name__,template_folder='template')
# @app.route("/")
# def hello_world():
#     return "Welcome to world of AI"

@app.route("/")
def index():
    # return "<h1 style='color:red'>This is second route</h1>"
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict_surviving():
    # return "<h1 style='color:red'>This is second route</h1>"
    Pclass=float(request.form.get("Pclass"))
    Sex=str(request.form.get("Sex"))
    Age=float(request.form.get("Age"))
    SibSp=int(request.form.get("SibSp"))
    Parch=float(request.form.get("Parch"))
    Fare=float(request.form.get("Fare"))
    Embarked=str(request.form.get("Embarked"))
    
    resul=model.predict(np.array([Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]))
    
    if resul[0]==1:
        resul = "Sur"
    else:
        resul = "not"
    return render_template("index.html",resul=resul)
app.run(debug=True)