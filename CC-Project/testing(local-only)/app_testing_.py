from flask import Flask, redirect,request,render_template,url_for,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../testing(local-only)/database.db'
db = SQLAlchemy(app)

class user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))

@app.route("/")
def home():
    return "Hello, Flask! Its Work!!"


@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        emailmu = request.form["emailmu"]
        passwdmu = request.form["passwdmu"]

        login = user.query.filter_by(email=emailmu, password=passwdmu).first()

        if login is not None:
            return redirect(url_for("home"))
    return render_template("test-login.html")

 
@app.route("/register",methods=["GET", "POST"])
def register():
    if request.method == "POST":
        namalngkpmu = request.form['namalngkpmu']
        emailmu = request.form['emailmu']
        passwdmu = request.form['passwdmu']

        register = user(full_name = namalngkpmu, email = emailmu, password = passwdmu)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("test-register.html")
    
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)