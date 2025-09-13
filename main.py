from flask import Flask, render_template, request


app = Flask(__name__)

listaDatos = []

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


#XD

def guardar():  
    datoObtenido = ""
    if request.method == 'POST':
        datoObtenido = request.form['in_nombres']
        print(datoObtenido)
    

if __name__ == '__main__':
    app.run(debug=True)
