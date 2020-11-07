from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! 😎\n'

@app.route('/20sec')
def tsec():
    time.sleep(20)
    return '20 sec'

app.run(host='0.0.0.0')