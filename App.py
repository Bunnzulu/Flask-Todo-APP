from flask import Flask,render_template,request
from Database import Add_Account,Get_Accounts

app = Flask(__name__ ,template_folder= "Templates")
ACCOUNTS = Get_Accounts()
@app.route('/')  #Basically what shows on home page
def Login_Screen():
    return render_template("Login_Screen.html",Accounts=ACCOUNTS)


@app.route('/Sign-up')  
def Sign_Up_Screen():
    UserNames = [name["username"] for name in ACCOUNTS]
    with open("UserNames.txt","w") as file:
        for Name in UserNames: 
            file.write(Name)
            file.write("\n")
    return render_template("Sign_up.html")


@app.route('/Signed-up',methods=["post"])  
def Signed_Up_Screen():
    data = request.form
    New_account = Add_Account(data)
    if New_account:return render_template("ConfirmSign-in.html")
    else:return render_template("BadUserName.html")

if __name__ == '__main__':
    app.run(debug=True)