import os
import pickle
from urllib import request
from django.conf import settings
from django.shortcuts import render

# Load model with error handling
model = None
try:
    model_path = os.path.join(settings.BASE_DIR, 'dtc.pkl')
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    print(f"Warning: Could not load ML model: {e}")
    model = None

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

        if model is not None:
            cust_env=[[age, gend, impul, pressure_high, pressure_low, glucose, trop]]
            pred=model.predict(cust_env)
            print("Prediction:", pred)
        else:
            pred = ["Model not available - deployment in progress"]
            print("Model not loaded, showing placeholder")
    return render(request, "home.html", {'prediction': pred})

def about(request):
    return render(request, "about.html")
def contact(request):   
    return render(request, "contact.html")
