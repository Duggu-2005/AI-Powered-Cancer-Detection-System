from django.shortcuts import render
import pickle
import numpy as np

model = pickle.load(open(r'C:\Users\Hp\Desktop\ml\model.pkl','rb'))
scaler = pickle.load(open(r'C:\Users\Hp\Desktop\ml\sc.pkl','rb'))
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