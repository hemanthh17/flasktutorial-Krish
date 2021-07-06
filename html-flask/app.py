## Integrate HTML with Flask
## DO GET and POST
from flask import Flask, request,redirect, url_for, render_template

app= Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')
#VARIABLE RULES METHOD

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)
@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the mark is "+str(score)

@app.route('/results/<int:score>')
def results(score):
    result=''
    if score<50:
        result="fail"
    else:
        result="success"
    #return result
    return redirect(url_for(result,score=score))

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
        
        return redirect(url_for('success',score=total_score))



if __name__=="__main__":
    app.run(debug=True)