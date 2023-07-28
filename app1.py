from flask import Flask,request,redirect,url_for,render_template

app=Flask(__name__)

@app.route("/success/<name>")
def success(name):
    return "Welcome %s" %name

@app.route("/login",methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        #user = request.args.get('nm')
        #return redirect(url_for('success',name=user))
        return render_template("login.html")

if __name__=="__main__":
    app.run()
    
