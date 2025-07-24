from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")

        new_user = User(name=name, age=age)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("home"))

    users = User.query.all()
    return render_template("home.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
