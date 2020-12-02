from flask import Flask

app = Flask(__name__)

@app.route('/<name>')

def hello_world (name):
    return f"<h1>Hello</h1> <h2> {name}</h2>"

if __name__ == "__main__" :
    app.run(debug=True)
