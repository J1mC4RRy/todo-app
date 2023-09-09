from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample initial todo list
todos = [
    {"id": 1, "task": "Learn Flask", "done": False},
    {"id": 2, "task": "Build a To-Do App", "done": True},
]

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add_todo():
    task = request.form.get("task")
    if task:
        new_id = max([todo["id"] for todo in todos]) + 1
        todos.append({"id": new_id, "task": task, "done": False})
    return redirect(url_for("index"))

@app.route("/toggle/<int:todo_id>")
def toggle_todo(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = not todo["done"]
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
