from flask import Flask, jsonify, request, send_file, render_template

app = Flask(__name__)


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    # defining function
    return render_template("404.html")


if __name__ != '__main__':
    raise Exception("Could not start server due to unknown application name")

####################
# HTTP ROUTES
####################


@app.route('/test', methods=['GET'])
def index():
    return "Test page"

####################
# START APPLICATION
####################


app.run(debug=True, port=8000, host="localhost")
