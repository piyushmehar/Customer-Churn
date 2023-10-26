from flask import Flask , render_template,request
import numpy as np
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl' ,'rb'))

@app.route('/')
def hello():
    return render_template("index1.html")

@app.route('/predict', methods=['POST'])
def predict():
    
    #for putting the details on the html GUI

    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # print(final_features)
    # prediction = model.predict(final_features)
    # output = round(prediction[0], 2)

    # customerid = request.form.get('customerid')
    creditscore = request.form.get('creditscore')
    city = request.form.get('city')
    gender = request.form.get('gender')
    age = request.form.get('age')
    tenure = request.form.get('tenure')
    balance = request.form.get('balance')
    noofproduct = request.form.get('noofproduct')
    havecrcard = request.form.get('havecrcard')
    isactivemember = request.form.get('isactivemember')
    estimatedsalary = request.form.get('estimatedsalary')

    int_features = [creditscore,city,gender,age,tenure,balance,noofproduct,havecrcard,isactivemember,estimatedsalary]
    final_features = [np.array(int_features)]
    print(final_features)
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    if(output==0):
        return render_template('index1.html', prediction_text='Customer will Stay'.format(output))
    elif(output==1):
        return render_template('index1.html', prediction_text='Customer will leave'.format(output))
    


if __name__=="__main__":
    app.run()
