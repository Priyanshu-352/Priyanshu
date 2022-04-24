from flask import Flask as f
from views import views

app = f(__name__)
app.register_blueprint(views, url_prefix="/views")


@app.route("/")
def home():
    return "this is the home page "

if __name__ =="__main__":
    app.run(debug=True ,port=8000)
