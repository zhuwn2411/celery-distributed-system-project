from flask import Flask, jsonify
from tasks import add, celery

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h2>Celery Distributed Task Queue</h2>

    <p>Tạo task:</p>
    <a href="/add/5/10">/add/5/10</a>
    """

# Tạo task mới
@app.route('/add/<int:x>/<int:y>')
def create_task(x, y):

    task = add.delay(x, y)

    return jsonify({
        "task_id": task.id,
        "status": "PENDING"
    })

# Theo dõi trạng thái task
@app.route('/status/<task_id>')
def check_status(task_id):

    task = celery.AsyncResult(task_id)

    response = {
        "task_id": task.id,
        "status": task.status
    }

    if task.status == "SUCCESS":
        response["result"] = task.result

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)