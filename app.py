from flask import Flask, render_template, request
# import sqlite3

app = Flask(__name__)

#Home route to render the input form
@app.route('/')
def index():
    return "hello World!"


if __name__ == "__main__":
    app.run(debug=True)