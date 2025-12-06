from django.shortcuts import render
import pickle
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")
model = pickle.load(open(model_path, "rb"))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "sc.pkl")
scaler = pickle.load(open(model_path, "rb"))
def first(request):
    return render(request,'index.html')

def predict(request):
    input_data = request.POST.get('input')
    features = list(map(float, input_data.split(',')))

    arr = np.array(features).reshape(1, -1)

    # SCALE INPUT FIRST
    arr = scaler.transform(arr)

    # Predict
    pred = model.predict(arr)[0]

    output = "cancerous" if pred == 1 else "not cancerous"

    return render(request, 'index.html', {'message': output})
