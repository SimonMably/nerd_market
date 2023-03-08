from flask import render_template
from app import bp


@bp.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", title="Home")


