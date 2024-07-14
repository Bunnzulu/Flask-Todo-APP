from flask import Flask,render_template

app = Flask(__name__ ,template_folder= "Templates")

@app.route('/')  #Basically what shows on home page
def Login_Screen():
    return render_template("Login_Screen.html")






if __name__ == '__main__':
    app.run(debug=True)