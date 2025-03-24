from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()
    code = data["code"]
    
    try:
        result = subprocess.run(["python", "-c", code], capture_output=True, text=True, timeout=5)
        return result.stdout if result.stdout else result.stderr
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
