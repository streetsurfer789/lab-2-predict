from flask import Flask, render_template
from sklearn import datasets, linear_model
from sklearn.externals import joblib

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", prediction=model.predict([[4, 2.5, 3005, 15, 17903.0,0,1]]).round(1))

if __name__=="__main__":
	model = joblib.load('regr3.pkl')
	app.run(debug=True)