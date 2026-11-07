
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if not path:
        path = "login.html"

    return send_from_directory(
        os.path.dirname(os.path.abspath(__file__)),
        path
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
