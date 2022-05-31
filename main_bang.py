from flask import Flask, render_template,request,jsonify
import json
import util

app= Flask(__name__)
#data= pd.read_csv("Cleaned_data.csv")
locations=None
data_columns=None

@app.route('/')
def index():
    global locations
    global data_columns
    with open("columns_Banglore.json", 'r') as f:
        data_columns = json.load(f)['data_columns']
        locations = data_columns[3:]

    return render_template('index1.html', location=locations)

@app.route('/predict', methods=['POST'])
def predict():
    locations= request.form.get('location')
    bhk=int(request.form.get('BHK'))
    bath=int(request.form.get('Bath'))
    total_sqft=float(request.form.get('total_sqft'))
    prediction = jsonify(
        util.get_estimated_price_bang(locations, total_sqft, bhk, bath)
    )

    return prediction

if __name__== "__main__":
    util.load_saved_artifacts1()
    app.run(debug=True, port=5001)
