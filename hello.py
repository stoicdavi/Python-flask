from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World This is!'

@app.route('/admin/<name>')
def hello_admin(name):
    return 'Hello Admin %s' % name

@app.route("/user/<name>")
def hello_user(name):
    return 'Hello %s!' % name

def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    
    elif name == 'user':
        return redirect(url_for('hello_user', name='admin'))
    else:
        return redirect(url_for('hello_world'))
if __name__ == '__main__':
    app.run(port='5001', debug=True)
