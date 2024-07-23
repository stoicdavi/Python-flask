from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/results', methods=['POST', 'GET'])
def results():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result=result)


if __name__== '__main__':
    app.run(port='5001', debug=True)
