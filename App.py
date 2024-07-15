from flask import Flask,render_template

app = Flask(__name__ ,template_folder= "Templates")

@app.route('/',methods=["post"])  #Basically what shows on home page
def Login_Screen():
    return render_template("Login_Screen.html")


@app.route('/Sign-up')  
def Sign_Up_Screen():
    return render_template("Sign_up.html")




if __name__ == '__main__':
    app.run(debug=True)