from flask import Flask, request, render_template 

app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 

def teste():
    erro = None
    imc = None
    res = None

    if request.method == "POST":
        try:
            peso = float(request.form['peso'])
            altura = float(request.form['altura'])
            if altura == 0 or peso == 0:
                erro = "Altura ou peso não podem ser 0"
            else:
                imc = peso / (altura ** 2)
        except ValueError:
            erro = "Valores inválidos"
    
    if imc is not None:
        if imc <= 16:
            res = "Extremamente baixo"
        elif imc <= 17:
            res = "Muito baixo"
        elif imc <= 18.5:
            res = "Baixo"
        elif imc <= 25:
            res = "Normal"
        elif imc <= 30:
            res = "Alto"
        elif imc <= 38:
            res = "Muito alto"
        else:
            res = "Extremamente alto"
    return render_template('index.html', imc=imc, res=res, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)



