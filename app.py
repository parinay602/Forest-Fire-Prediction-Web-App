from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
#from flask_mysqldb import MySQL

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("forest_fire.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('index_danger.html',pred=output)
    else:
        return render_template('index_safe.html',pred=output)


if __name__ == '__main__':
    app.run(debug=True)

