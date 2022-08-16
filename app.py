from flask import Flask, request,render_template
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def HomePage():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            Pclass = int(request.form['Pclass'])
            SibSp = int(request.form['SibSp'])
            Parch = int(request.form['Parch'])
            Age = float(request.form['Age'])
            Fare = float(request.form['Fare'])
            is_male = int(request.form['male'])
            if (is_male == 'male'):
                male = 1
            else:
                male = 0
            filename = 'titanic_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))
            prediction = loaded_model.predict([[Pclass, SibSp,Parch,Age,Fare,is_male]])
            return render_template('results.html',prediction=prediction[0])
        except Exception as e:
            print("The exception is:", e)
            return "Something is wrong"
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
    #app.run(debug=True)