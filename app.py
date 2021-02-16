from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = [0]
    if request.method == 'POST':
        model = pickle.load(open('model.pkl', 'rb'))
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        c = float(request.form.get('c'))
        d = float(request.form.get('d'))
        e = float(request.form.get('e'))
        f = float(request.form.get('f'))
        g = float(request.form.get('g'))
        h = float(request.form.get('h'))
        i = float(request.form.get('i'))
        j = float(request.form.get('j'))
        prediction = model.predict([[a, b, c, d, e, f, g, h, i, j]])
        print(prediction)
        if prediction == [1]:
            prediction= 'Qualifié'
        else:
            prediction= 'Non qualifié'

    return render_template('after.html', prediction=prediction)

