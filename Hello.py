from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import g
app = Flask(__name__)


@app.before_request
def before_request():
    return
    #g.db = connect_db


@app.teardown_request
def teardown_request(exception):
    return
    #g.db.close


@app.route("/")
def hello():
    return "I like turtles!"


@app.route("/profile")
def profile():
    return render_template("profile.html")
    #return "Create a new profile."



@app.route("/profiles", methods=["GET", "POST"])
def profiles():
    if request.method == "POST":
        #return jsonify output
        return jsonify(username=g.user.username, email=g.user.useremail, id=g.user.userid)
    else:
        return render_template("profiles.html")
    #return "List of all profiles."


@app.route("/profile/<userid>", methods=["GET", "POST"])
def profileid(userid):
    return render_template("profileid.html", userid=userid)
    #return "This profile belongs to " + userid

if __name__ == "__main__":
    app.run()
