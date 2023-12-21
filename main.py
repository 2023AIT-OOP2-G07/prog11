from flask import Flask
from upload import uploadBluePrint
from list import list_page

app = Flask(__name__)
app.register_blueprint(uploadBluePrint)
app.register_blueprint(list_page)

if __name__ == "__main__":
    app.run(debug=True)
