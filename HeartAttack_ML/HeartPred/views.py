import os
import pickle
from urllib import request
from django.conf import settings
from django.shortcuts import render

# Load model with error handling
model = None
model_error = None

def load_model():
    global model, model_error
    if model is not None:
        return model

    # Try multiple possible paths for the model file
    possible_paths = [
        os.path.join(settings.BASE_DIR, 'dtc.pkl'),
        os.path.join(settings.BASE_DIR, 'HeartAttack_ML', 'dtc.pkl'),
        os.path.join(os.path.dirname(__file__), '..', 'dtc.pkl'),
        os.path.join(os.path.dirname(__file__), '..', '..', 'HeartAttack_ML', 'dtc.pkl'),
        'dtc.pkl',
        'HeartAttack_ML/dtc.pkl'
    ]

    for model_path in possible_paths:
        try:
            if os.path.exists(model_path):
                print(f"Found model at: {model_path}")
                with open(model_path, 'rb') as file:
                    model = pickle.load(file)
                print("Model loaded successfully!")
                return model
        except Exception as e:
            print(f"Failed to load model from {model_path}: {e}")
            model_error = str(e)

    print("Could not find model file in any of the expected locations")
    print(f"BASE_DIR: {settings.BASE_DIR}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Files in BASE_DIR: {os.listdir(settings.BASE_DIR) if os.path.exists(settings.BASE_DIR) else 'BASE_DIR not found'}")

    return None

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

        # Try to load the model
        current_model = load_model()

        if current_model is not None:
            try:
                # Convert inputs to appropriate types
                cust_env=[[int(age), int(gend), int(impul), int(pressure_high), int(pressure_low), int(glucose), float(trop)]]
                pred=current_model.predict(cust_env)
                print("Prediction:", pred)
            except Exception as e:
                pred = [f"Prediction error: {str(e)}"]
                print(f"Prediction error: {e}")
        else:
            pred = [f"Model not available - Error: {model_error if model_error else 'Unknown error'}"]
            print("Model not loaded, showing error message")
    return render(request, "home.html", {'prediction': pred})

def about(request):
    return render(request, "about.html")
def contact(request):   
    return render(request, "contact.html")
