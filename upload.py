from flask import Blueprint, render_template, request, jsonify
import os

uploadBluePrint = Blueprint("upload", __name__)


@uploadBluePrint.route("/", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        # Do something with the file
        # file = request.files["file"]
        # file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
        if file.filename == "":
            render_template("index.html", msg="No file selected")
        elif file:
            # filename = secure_filename(file.filename)
            filename = file.filename
            # file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            file.save(os.path.join("static/images/upload", filename))
        return render_template("index.html", msg="File uploaded successfully")
    elif request.method == "GET":
        return render_template("index.html")
