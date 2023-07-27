from flask import Flask,render_template,redirect,url_for,request


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ToDo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key = True)
    title=db.Column(db.String(200),nullable =False)
    value1 = db.Column(db.String(500),nullable =False)
    date_created=db.Column(db.DateTime,default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title} "

@app.route("/",methods =["GET","POST"])
def Home():
    if request.method=="POST":
        title =request.form['title']
        value1=request.form['value1']
        todo=Todo(title = title,value1 = value1)
        db.session.add(todo)
        db.session.commit()
    alltodo =Todo.query.all()
    print(alltodo)
    return render_template("todo.html",alltodo=alltodo)
# Just an easy methods

@app.route("/show")
def show():
    alltodo =Todo.query.all()
    print(alltodo)
    return "This iis product page"

@app.route("/welcome")
def welcome():
    return "<h1>welcome to the flask tutorial.</h1>"
# For rendering templates
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/result/<int:score>")
def check(score):
    if score >= 60:
        return f"You passed this test"
    else:
        return "You failed this exam."

@app.route("/success/<int:score>")
def success(score):
    
    return f"You got passed and your score is {score}"

@app.route("/fail/<int:score>")
def fail(score):
    
    return f"You got failed and your score is {score}"

@app.route("/calculate",methods=['POST','GET'])
def calculate():
    if request.method=="GET":
        return render_template("calculate.html")
    else:
        math=float(request.form["maths"])
        scince =float(request.form["scince"])
        social_scince=float(request.form["social scince"])
        avgs = (math+scince+social_scince)/3
        
        # if avgs >=50:
            # result="success"
        # else:
            # result ="fail"
        
        #return redirect(url_for(result,score=avgs))
        return render_template("index.html",results=avgs)

if __name__=="__main__":
    #with app.app_context():
     #   db.create_all()
    app.run(debug=True)