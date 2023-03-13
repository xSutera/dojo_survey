from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def page2():
    session['name']=request.form['name']
    session['langauge']=request.form['langauge']
    session['comments']=request.form['comments']
    session['location']=request.form['location']

    return redirect('/results')

@app.route('/results')
def page3():
    return render_template('results.html')

if __name__ =="__main__":
    app.run(debug=True)