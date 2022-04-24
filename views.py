from flask import Blueprint as b,render_template ,request,jsonify,redirect,url_for



views = b(__name__,"Views")


@views.route("/")
def home():
    return render_template("index.html" , name ="I AM PRIYANSHU WHAT WOULD YOU LIKE TO KNOW ABOUT ME ")

@views.route("/profile/")
def profile():
    return render_template("index.html" , name ="priyanshu")

@views.route("/json")
def get_json():
    return jsonify({"name" : "sunny", "coolness" : "100+" })


@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))