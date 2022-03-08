from django.shortcuts import render, redirect
from django.http import HttpResponse
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
# Create your views here.


def dietician(request):
    prediction = None
    mealplan = None
    e = None
    global g
    df = pd.read_csv(
        'D:\Study Material\SEM 8\CSE 445\Capstone Project\Capstone_Project\Live_Fit\media\Diet.csv', encoding='cp1252')

    X_train = df.loc[:, 'Gender':'Exercise']
    Y_train = df.loc[:, 'Diet']

    # The actual decision tree classifier
    tree = DecisionTreeClassifier(max_leaf_nodes=5, random_state=0)

    # Train the model
    tree.fit(X_train.values, Y_train.values)

    if request.method == 'POST':
        age = request.POST['age']
        gender = request.POST['gender']
        exercise = request.POST['exercise']

        if gender == 'Male':
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

        prediction = tree.predict([[g, age, e]])

        mealplan = str(prediction[0]).split('\n')

    return render(request, 'dietician/dietician.html', {'mealplan': mealplan})
