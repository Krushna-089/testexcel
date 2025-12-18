from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('form.html')

@app.route('/success', methods=['POST'])
def ptintdata():
    result = request.form
    return render_template('result.html', result=result)

if __name__ == '__main__':

    app.run(debug=True)
