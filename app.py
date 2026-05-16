from datetime import datetime
from flask import Flask, render_template, request, redirect

app = Flask(__name__)



tasks = [{"title_name": "Task 1", "done": False}]

@app.route('/')
def index():
    current_date = datetime.now().strftime("%A %d %b,%Y")
    return render_template('index.html',tasks=tasks,today=current_date)

@app.route('/add',methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({"title_name": task, "done":False})
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect('/')

@app.route('/select/<int:index>')
def select_task(index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = not tasks[index]['done']
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)

