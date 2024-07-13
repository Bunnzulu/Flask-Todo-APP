from flask import Flask

app = Flask(__name__ ,template_folder= "Templates")

@app.route('/')  #Basically what shows on home page
def hello_World():
    return "Hello World"






if __name__ == '__main__':
    app.run(debug=True)