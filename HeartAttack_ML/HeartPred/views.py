import os
import pickle
from urllib import request
from django.conf import settings
from django.shortcuts import render

model=os.path.join(settings.BASE_DIR, 'dtc.pkl')
with open(model, 'rb') as file:
    model=pickle.load(file)

def home(request):
    pred=None
    if request.method=="POST":
        age= request.POST['age']
        gend= request.POST['gender']
        impul = request.POST['impulse']
        pressure_high = request.POST['pressurehight']
        pressure_low = request.POST['pressurelow']
        glucose = request.POST['glucose']
        trop = request.POST['troponin']

        print("Age:", age)
        print("Gender:",gend)
        print("Impulse:", impul)
        print("Preesure High:", pressure_high)
        print("Preesure Low:", pressure_low)    
        print("Glucose:", glucose)
        print("Troponin:", trop)

        cust_env=[[age, gend, impul, pressure_high, pressure_low, glucose, trop]]
        pred=model.predict(cust_env)
        print("Prediction:", pred)
    return render(request, "home.html", {'prediction': pred})

def about(request):
    return render(request, "about.html")
def contact(request):   
    return render(request, "contact.html")
