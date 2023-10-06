from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    if "name" in request.args:
        name = request.args["name"]
    else:
        name = "world"
    return render_template("index.html", name = name)
    
    """
    careful of indetation
    Sample Flask app
    or you can implement like this 2nd parameter world is for default can change to any 4 lines of code into 1 per documentation no if else
    this returns null value if there is no value 
    name = request.args.get("name", "world")
    return render_template("index.html", name = name)
    """
