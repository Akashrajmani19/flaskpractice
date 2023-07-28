from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/' ,methods =['GET','POST'])
def squarenum():
    if request.method == "GET":
        return render_template("squarenum.html")
    else:
        num=request.form['num']
        square=(int(num))**2
        return render_template("square_num_result.html",value=square,num=num)



if __name__=="__main__":
    app.run(debug=True)