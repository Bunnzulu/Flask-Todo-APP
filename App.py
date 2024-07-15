from flask import Flask,render_template,request
from Database import Add_Account

app = Flask(__name__ ,template_folder= "Templates")

@app.route('/')  #Basically what shows on home page
def Login_Screen():
    return render_template("Login_Screen.html")


@app.route('/Sign-up')  
def Sign_Up_Screen():
    return render_template("Sign_up.html")

@app.route('/Signed-up',methods=["post"])  
def Signed_Up_Screen():
    data = request.form
    Add_Account(data)
    return render_template("Sign_up.html")


if __name__ == '__main__':
    app.run(debug=True)