from flask import Flask, render_template,request

myflask=Flask(__name__)

@myflask.route('/',methods=['GET','POST'])

def user():
    if request.method=='POST':
        name=request.form.get('username')
        print(f'Hi {name},welcome to my web page')
    return render_template('userdata.html')

if __name__=='__main__':
    myflask.run(debug=True)    
