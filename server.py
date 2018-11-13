from flask import Flask, render_template, session, redirect, request, flash

app=Flask(__name__)
app.secret_key = "98jeofijejfqiwefso8i"

print(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print('Got post information')
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']

    if len(request.form['name'])<1:
        flash('Name can not be blank.', 'name')
    elif len(request.form['name']) <3:
        flash('Name must be longer than 3+ characters.', 'name')
    
    if len(request.form['comments'])<1:
        flash('Comments must not be blank.')

    elif len(request.form['comments'])>120:
        flash('Comments must be less than 120 Characters.')
    
    if '_flash' in session:
        return redirect('/')
    else:
        return render_template('/result.html')


# @app.route('/result')
# def result():
#     pass


if __name__ == "__main__":
    app.run(debug=True)
