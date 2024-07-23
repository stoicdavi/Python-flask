from flask import Flask, session, redirect, url_for, request, render_template
app =Flask(__name__)
app.secret_key = 'kwydavi'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as '+username+'<br>'+\
        "<b><a href='/logout'> logout</a></b>"
    return "You are not logged in <br><a href='/login'><b>" + \
            " click to Login </b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port='5002', debug=True)