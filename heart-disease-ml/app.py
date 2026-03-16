from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import joblib
import pandas as pd
import os

app = Flask(__name__)

model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")

EXCEL_FILE = "users.xlsx"


# PAGE 1
@app.route("/")
def access():
    return render_template("access.html")


@app.route("/save_user", methods=["POST"])
def save_user():

    name = request.form["name"]
    email = request.form["email"]

    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE)
        new_id = df["ID"].max() + 1
    else:
        df = pd.DataFrame(columns=["ID","Name","Email"])
        new_id = 1

    new_row = pd.DataFrame({
        "ID":[new_id],
        "Name":[name],
        "Email":[email]
    })

    df = pd.concat([df,new_row], ignore_index=True)
    df.to_excel(EXCEL_FILE,index=False)

    return redirect(url_for("prediction_page"))


# PAGE 2
@app.route("/predict_page")
def prediction_page():
    return render_template("index.html")


# PAGE 3
@app.route("/predict", methods=["POST"])
def predict():

    try:

        age = float(request.form.get('age'))
        sex = float(request.form.get('sex'))
        cp = float(request.form.get('cp'))
        trestbps = float(request.form.get('trestbps'))
        chol = float(request.form.get('chol'))
        fbs = float(request.form.get('fbs'))
        restecg = float(request.form.get('restecg'))
        thalach = float(request.form.get('thalach'))
        exang = float(request.form.get('exang'))
        oldpeak = float(request.form.get('oldpeak'))
        slope = float(request.form.get('slope'))
        ca = float(request.form.get('ca'))
        thal = float(request.form.get('thal'))

        features = np.array([[age,sex,cp,trestbps,chol,fbs,
                              restecg,thalach,exang,oldpeak,
                              slope,ca,thal]])

        features = scaler.transform(features)

        probability = model.predict_proba(features)[0][1]
        prob_percent = round(probability*100,2)

        if prob_percent < 30:
            risk = "Low Risk"
        elif prob_percent < 60:
            risk = "Moderate Risk"
        else:
            risk = "High Risk"

        issues = []

        if age > 55:
            issues.append("Higher age increases cardiovascular risk")

        if chol > 240:
            issues.append("High cholesterol level detected")

        if trestbps > 140:
            issues.append("High resting blood pressure")

        if thalach < 100:
            issues.append("Low maximum heart rate")

        if oldpeak > 2:
            issues.append("ST depression indicates heart stress")

        if exang == 1:
            issues.append("Exercise induced angina present")

        if len(issues) == 0:
            issues.append("No major risk indicators detected")

        return render_template(
            "result.html",
            probability=prob_percent,
            risk=risk,
            issues=issues
        )

    except:
        return redirect(url_for("prediction_page"))


if __name__ == "__main__":
    app.run(debug=True)