import flask  # import flask

app = flask.Flask(__name__)  # create an app instance


@app.route("/")  # at the end point /
def main():  # call method main
    return flask.render_template("template.html")


@app.route("/baileyluu")  # at the end point /
def bailey():  # call method bailey
    return flask.redirect(
        "http://baileyluu.tech")  # which redirect to my portfolio website


if __name__ == "__main__":  # on running python app.py
    app.run(host="0.0.0.0", port=5000, debug=True)  # run the flask app
