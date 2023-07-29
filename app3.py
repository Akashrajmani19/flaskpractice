from flask import Flask,request,render_template,jsonify
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<p>Welcome To the Flask.</p>"

# @app.route("/cal" ,methods =["GET"])
# def meth_operation():
#     operation = request.json["operation"]
#     number1 =int(request.json["number1"])
#     number2 =int(request.json["number2"])

#     if operation=="add":
#         result= number1+number2
#     elif operation=="multiply":
#         result = number1*number2
#     elif operation=="division":
#         result = number1/number2
#     else:
#         result = number1-number2
#     return f"Our operation {operation} on number1 :{number1} and number2 : {number2} got result :{result}"

@app.route("/cal" ,methods =["POST","GET"])
def meth_operation():
    if request.method=="POST":
        operation = str(request.form["operation"])
        number1 =int(request.form["number1"])
        number2 =int(request.form["number2"])

        if operation=="add":
            result= number1+number2
        elif operation=="multiply":
            result = number1*number2
        elif operation=="division":
            result = number1/number2
        else:
            result = number1-number2
        return render_template("result.html",operation=operation,result=result,number1=number1,number2=number2)
    else:
        return render_template("cal.html")


if __name__=="__main__":
    app.run()