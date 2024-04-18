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
ochkicomand2 = "0"
ochkicomand3 = "0"
ochkicomand4 = "0"
ochkicomand5 = "0"
ochkicomand6 = "0"
ochkicomand7 = "0"
ochkicomand8 = "0"

@app.route('/')
def index():
    return render_template('index.html', comand1=comand1, ochkicomand1=ochkicomand1,comand2=comand2,comand3=comand3,comand4=comand4,comand5=comand5,comand6=comand6,comand7=comand7,comand8=comand8, ochkicomand2=ochkicomand2, ochkicomand3=ochkicomand3, ochkicomand4=ochkicomand4, ochkicomand5=ochkicomand5, ochkicomand6=ochkicomand6, ochkicomand7=ochkicomand7, ochkicomand8=ochkicomand8)

@app.route('/panel')
def panel():
    return render_template('panel.html')

@app.route('/save', methods=['POST'])
def save():
    global comand1, ochkicomand1, comand2, comand3, comand4, comand5, comand6, comand7, comand8, ochkicomand2, ochkicomand3, ochkicomand4, ochkicomand5, ochkicomand6, ochkicomand7, ochkicomand8

    comand1 = request.form['comand1']
    comand2 = request.form['comand2']
    comand3 = request.form['comand3']
    comand4 = request.form['comand4']
    comand5 = request.form['comand5']
    comand6 = request.form['comand6']
    comand7 = request.form['comand7']
    comand8 = request.form['comand8']
    ochkicomand1 = request.form['ochkicomand1']
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
