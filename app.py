from flask import Flask, render_template, request, redirect

app = Flask(__name__)

comand1 = ""
comand2 = ""
comand3 = ""
comand4 = ""
comand5 = ""
comand6 = ""
comand7 = ""
comand8 = ""
ochkicomand1 = "0"
ochkicomand11 = "0"
ochkicomand111 = "0"
ochkicomand1111 = "0"
ochkicomand11111 = "0"
ochkicomand111111 = "0"
ochkicomand1111111 = "0"
ochkicomand2 = "0"
ochkicomand22 = "0"
ochkicomand222 = "0"
ochkicomand2222 = "0"
ochkicomand22222 = "0"
ochkicomand222222 = "0"
ochkicomand2222222 = "0"
ochkicomand3 = "0"
ochkicomand33 = "0"
ochkicomand333 = "0"
ochkicomand3333 = "0"
ochkicomand33333 = "0"
ochkicomand333333 = "0"
ochkicomand3333333 = "0"
ochkicomand4 = "0"
ochkicomand44 = "0"
ochkicomand444 = "0"
ochkicomand4444 = "0"
ochkicomand44444 = "0"
ochkicomand444444 = "0"
ochkicomand4444444 = "0"
ochkicomand5 = "0"
ochkicomand55 = "0"
ochkicomand555 = "0"
ochkicomand5555 = "0"
ochkicomand55555 = "0"
ochkicomand555555 = "0"
ochkicomand5555555 = "0"
ochkicomand6 = "0"
ochkicomand66 = "0"
ochkicomand666 = "0"
ochkicomand6666 = "0"
ochkicomand66666 = "0"
ochkicomand666666 = "0"
ochkicomand6666666 = "0"
ochkicomand7 = "0"
ochkicomand77 = "0"
ochkicomand777 = "0"
ochkicomand7777 = "0"
ochkicomand77777 = "0"
ochkicomand777777 = "0"
ochkicomand7777777 = "0"
ochkicomand8 = "0"
ochkicomand88 = "0"
ochkicomand888 = "0"
ochkicomand8888 = "0"
ochkicomand88888 = "0"
ochkicomand888888 = "0"
ochkicomand8888888 = "0"

ochkicomand2 = "0"
ochkicomand3 = "0"
ochkicomand4 = "0"
ochkicomand5 = "0"
ochkicomand6 = "0"
ochkicomand7 = "0"
ochkicomand8 = "0"

@app.route('/')
def index():
    return render_template('index.html',comand1=comand1, ochkicomand1=ochkicomand1,comand2=comand2,comand3=comand3,comand4=comand4,comand5=comand5,comand6=comand6,comand7=comand7,comand8=comand8, ochkicomand2=ochkicomand2, ochkicomand3=ochkicomand3, ochkicomand4=ochkicomand4, ochkicomand5=ochkicomand5, ochkicomand6=ochkicomand6, ochkicomand7=ochkicomand7, ochkicomand8=ochkicomand8)
 

@app.route('/panel')
def panel():
    return render_template('panel.html')

@app.route('/save', methods=['POST'])
def save():
    global comand1, ochkicomand1, ochkicomand11, ochkicomand111, ochkicomand1111, ochkicomand11111, ochkicomand111111, ochkicomand1111111, ochkicomand2, ochkicomand22, ochkicomand222, ochkicomand2222, ochkicomand22222, ochkicomand222222, ochkicomand2222222, ochkicomand3, ochkicomand33, ochkicomand333, ochkicomand3333, ochkicomand33333, ochkicomand333333, ochkicomand3333333, ochkicomand4, ochkicomand44, ochkicomand444, ochkicomand4444, ochkicomand44444, ochkicomand444444, ochkicomand4444444, ochkicomand5, ochkicomand55, ochkicomand555, ochkicomand5555, ochkicomand55555, ochkicomand555555, ochkicomand5555555, ochkicomand6, ochkicomand66, ochkicomand666, ochkicomand6666, ochkicomand66666, ochkicomand666666, ochkicomand6666666, ochkicomand7, ochkicomand77, ochkicomand777, ochkicomand7777, ochkicomand77777, ochkicomand777777, ochkicomand7777777, ochkicomand8, ochkicomand88, ochkicomand888, ochkicomand8888, ochkicomand88888, ochkicomand888888, ochkicomand8888888,ochkicomand1, comand2, comand3, comand4, comand5, comand6, comand7, comand8, ochkicomand2, ochkicomand3, ochkicomand4, ochkicomand5, ochkicomand6, ochkicomand7, ochkicomand8
 

    comand1 = request.form['comand1']
    comand2 = request.form['comand2']
    comand3 = request.form['comand3']
    comand4 = request.form['comand4']
    comand5 = request.form['comand5']
    comand6 = request.form['comand6']
    comand7 = request.form['comand7']
    comand8 = request.form['comand8']
    ochkicomand1 = request.form['ochkicomand1']
    ochkicomand11 = request.form['ochkicomand11']
    ochkicomand111 = request.form['ochkicomand111']
    ochkicomand1111 = request.form['ochkicomand1111']
    ochkicomand11111 = request.form['ochkicomand11111']
    ochkicomand111111 = request.form['ochkicomand111111']
    ochkicomand1111111 = request.form['ochkicomand1111111']
    ochkicomand2 = request.form['ochkicomand2']
    ochkicomand3 = request.form['ochkicomand3']
    ochkicomand4 = request.form['ochkicomand4']
    ochkicomand5 = request.form['ochkicomand5']
    ochkicomand6 = request.form['ochkicomand6']
    ochkicomand7 = request.form['ochkicomand7']
    ochkicomand8 = request.form['ochkicomand8']
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
