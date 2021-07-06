from flask import Flask, redirect, url_for

app= Flask(__name__)

@app.route('/')
def welcome():
    return "Hey hi welcome back"
#VARIABLE RULES METHOD

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the mark is "+str(score)
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


if __name__=="__main__":
    app.run(debug=True)