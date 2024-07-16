from flask import Flask,render_template,request
from Database import Add_Account,Get_Accounts,Verify_Cred,Add_to_Notes,Show_Notes,Delete_Note

app = Flask(__name__ ,template_folder= "Templates")
ACCOUNTS = Get_Accounts()
Login = [False,""]

@app.route('/')  #Basically what shows on home page
def Login_Screen():
    return render_template("Login_Screen.html")

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

@app.route('/Notes',methods=["post","get"])  
def Main_Screen():
    global Login
    data = request.form 
    if Verify_Cred(data) or Login:
        Login[0] = False
        if Login[1] == "": Login[1] = data.get("Username")
        if data.get("Username") == None: return render_template("MakinTodos.html",UserName=Login[1])
        return render_template("MakinTodos.html",UserName=data.get("Username"))
    else:return render_template("LoginError.html")

@app.route('/SavedNotes',methods=["post"])  
def TODO_Screen():
    global Login
    data = request.form 
    Add_to_Notes(data)
    Login[0] = True
    return render_template("SEEToDos.html",Needs=Show_Notes(data).split("/n")[:-1],UserName=data.get("Username"))

@app.route('/DeleteNotes',methods=["post"])  
def Deleted_Screen():
    global Login
    Login[0] = True
    data = request.form 
    Delete_Note(data)
    return render_template("ConfirmDeleted.html")


if __name__ == '__main__':
    app.run(debug=True)