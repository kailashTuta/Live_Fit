from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from .models import Report
from .forms import ReportForm
# Create your views here.


@login_required(login_url='login')
def dietician(request):
    df = pd.read_excel(
        r'D:\Study Material\SEM 8\CSE 445\Capstone Project\Capstone_Project\Live_Fit\media\Diet.xlsx', usecols=['Age', 'Gender', 'Exercise', 'Diabetic', 'Diet', 'Workouts'])

    cols = ['Gender', 'Age', 'Exercise', 'Diabetic']
    X_train = df.loc[:, cols]
    Y_train = df.loc[:, ['Diet', 'Workouts']]

    # The actual decision tree classifier
    tree = DecisionTreeClassifier(random_state=0)

    # Train the model
    tree.fit(X_train.values, Y_train.values)

    form = ReportForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            exercise = form.cleaned_data['exercise']
            diabetic = form.cleaned_data['diabetic']

            if diabetic == "no":
                d = 1
            elif diabetic == "yes":
                d = 2

            if gender == 'male':
                g = 1
            elif gender == 'female':
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
            # print(prediction[0][0])
            # print(prediction[0][1])

            mealplan = prediction[0][0].split('\n')
            mealplan = "<br><br>".join(mealplan)
            exerciseplan = prediction[0][1]

            bmi = int(weight) / (int(height)/100)**2

            instance = form.save(commit=False)
            instance.mealplan = mealplan
            instance.exerciseplan = exerciseplan
            instance.user = request.user
            instance.bmi = bmi

            if bmi <= 18.4:
                instance.remark = "You are underweight."
            elif bmi <= 24.9:
                instance.remark = "You are healthy."
            elif bmi <= 29.9:
                instance.remark = "You are over weight."
            elif bmi <= 34.9:
                instance.remark = "You are severely over weight."
            elif bmi <= 39.9:
                instance.remark = "You are obese."
            else:
                instance.remark = "You are severely obese."
            instance.save()
            form = ReportForm()
        else:
            form = ReportForm()
    context = {'form': form}
    return render(request, 'dietician/dietician.html', context)


@login_required(login_url='login')
def dietReport(request):
    context = {
        'user': request.user,
        'reports': Report.objects.filter(user=request.user)
    }
    return render(request, 'dietician/report.html', context)
