from django.shortcuts import render, redirect
from django.http import HttpResponse
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from .models import Report
# Create your views here.


def dietician(request):
    prediction = None
    mealplan = None
    e = None
    g = None
    d = None
    bmi = None
    remark = None
    df = pd.read_excel(
        r'D:\Study Material\SEM 8\CSE 445\Capstone Project\Capstone_Project\Live_Fit\media\Diet.xlsx')

    cols = ['Age', 'Gender', 'Exercise', 'Diabetic']
    X_train = df.loc[:, cols]
    Y_train = df.loc[:, 'Diet']

    # The actual decision tree classifier
    tree = DecisionTreeClassifier(random_state=0)

    # Train the model
    tree.fit(X_train.values, Y_train.values)

    if request.method == 'POST':
        name = request.POST['name']
        weight = request.POST['weight']
        height = request.POST['height']
        age = request.POST['age']
        gender = request.POST['gender']
        exercise = request.POST['exercise']
        diabetic = request.POST['diabetic']

        if diabetic == "no":
            d = 1
        elif diabetic == "yes":
            d = 2

        if gender == 'male':
            g = 1
        else:
            g = 2

        if exercise == 'sedentary':
            e = 1
        elif exercise == 'lightlyactive':
            e = 2
        elif exercise == 'moderate':
            e = 3
        elif exercise == 'veryactive':
            e = 4
        elif exercise == 'superactive':
            e = 5
        prediction = tree.predict([[g, age, e, d]])

        mealplan = str(prediction[0]).split('\n')
        bmi = int(weight) / (int(height)/100)**2

        if bmi <= 18.4:
            remark = "You are underweight."
        elif bmi <= 24.9:
            remark = "You are healthy."
        elif bmi <= 29.9:
            rmark = "You are over weight."
        elif bmi <= 34.9:
            remark = "You are severely over weight."
        elif bmi <= 39.9:
            remark = "You are obese."
        else:
            remark = "You are severely obese."
        r = Report(name=name, age=age, weight=weight, height=height,
                   bmi=bmi, gender=gender, diabetic=diabetic, exercise=exercise, remark=remark, mealplan=mealplan)
        r.save()

    return render(request, 'dietician/dietician.html', {'mealplan': mealplan, 'bmi': bmi, 'remark': remark})
