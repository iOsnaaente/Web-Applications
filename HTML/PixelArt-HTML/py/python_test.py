from flask import Flask , Blueprint

app = Flask(__name__)

app.register_blueprint(Blueprint('/html/table', __name__))


@app.route("/")
def hello():
    return "asasdasdasd"

app.run(debug = True, use_reloader=True)

