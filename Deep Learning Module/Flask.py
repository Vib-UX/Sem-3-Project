from flask import *
from Test_Flask import *

app = Flask(__name__)
app.debug = True

@app.route('/')

def hello():
    return render_template('index.html')

@app.route('/Download')

def call():
    load()
    
    
if __name__ == '__main__':
    app.run()
    
if __name__ == '__Download__':
    app.run()
