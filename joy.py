from flask import Flask,jsonify,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to postman demo"


@app.route("/result")
def addition():
    input_data=request.form
    print("The data is:",input_data)
    
    a=int(input_data['a'])
    b=int(input_data['b'])
    result=a+b
    
    return jsonify({"Result":f'Addition of {a} and {b} is {result}'})

@app.route("/multiply")
def mul():
    input_data=request.get_json()
    print("The data is:",input_data)
    
    a=int(input_data['a'])
    b=int(input_data['b'])
    result=a*b
    
    return jsonify({"Result":f'multiply of {a} and {b} is {result}'})

app.run(debug=True)