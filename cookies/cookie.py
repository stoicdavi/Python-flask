from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('setcookie.html')

@app.route('/setcookie', methods=['POST'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    if name:
        return f"<h1> Welcome {name} </h1>"
    else:
        return "<h1> No cookie found </h1>"

if __name__ == '__main__':
    app.run(port=5001, debug=True)
