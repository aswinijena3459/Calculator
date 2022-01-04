from flask import Flask,request,jsonify,render_template


app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_operations():
    if (request.method=='POST') :   ### for reading the request from the user request module is available
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])

        if operation=='add':
            r=num1+num2
            result='the addition of '+str(num1)+'and '+str(num2)+'is '+str(r)
        if operation=='mul':
            r=(num1*num2)
            result='the multiplication of '+str(num1)+'and '+str(num2)+'is '+str(r)
        if operation=='division':
            r=(num1/num2)
            result = 'the quotient after dividing ' + str(num1) + 'and ' + str(num2) + 'is ' + str(r)
        if operation=='subtract':
            r=(num1-num2)
            result='the subtraction of '+str(num1)+'and '+str(num2)+'is '+str(r)
        return render_template('results.html',result=result)







if __name__=='__main__':
    app.run(debug=True)