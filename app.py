from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    todoList = ['Finish this tutorial', 'Learn Flask', 'Promgrammieren', 'Profit!']
    return render_template('todo.html', todoList=todoList)

if __name__ == '__main__':
    app.run() 