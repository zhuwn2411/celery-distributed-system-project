from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Celery Distributed Task Queue"

if __name__ == '__main__':
    app.run(debug=True)