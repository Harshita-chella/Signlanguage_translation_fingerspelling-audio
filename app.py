from flask import Flask, render_template, request
import subprocess

app = Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signtotext', methods=['POST'])
def signtotext():
    subprocess.call(['python', 'test.py'])
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
