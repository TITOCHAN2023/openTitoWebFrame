from flask import Flask, render_template, request, jsonify
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<title>")
def test(title):
    return render_template(f"{title}.html")

@app.route("/menu/<title>")
def article_menu(title):
    return render_template(f"/menu/{title}.html")


@app.route("/article/<title>")
def article(title):
    return render_template(f"/article/{title}.html")

@app.route("/post/reg", methods=["POST"])
def do_register():
    print(request.form)
    return "register successfully"


@app.errorhandler(404)
def handle_404_error(err):
    return render_template('404.html')