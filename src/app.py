# import your files
from flask import Flask, render_template

# create your flask application
app = Flask(__name__)

# simple function that renders your html file


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # run your application with given host
