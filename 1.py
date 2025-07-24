from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    user_list=["silus","ragu","ravi","robert"]
    return render_template("home.html",use=user_list)
@app.route("/about/<int:score>")
def about(score):
    user="silus"
    age=22
    dd=score
    return render_template("about.html",score=dd)
if __name__ == "__main__":
 app.run(debug=True)
