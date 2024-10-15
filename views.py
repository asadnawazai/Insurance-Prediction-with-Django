from django.shortcuts import render
import joblib

# Load the trained model
model = joblib.load('F:/Insurance_project_Django/insurance_prediction/Random Forest')

def prediction(request):
    if request.method == 'POST':
        # Collect data from form
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))  # Expecting numeric values directly
        bmi = float(request.POST.get('bmi'))
        smoker = int(request.POST.get('smoker'))  # Expecting numeric values directly
        children = int(request.POST.get('children'))
        region = int(request.POST.get('region'))  # Expecting numeric values directly

        # Model prediction
        pred = model.predict([[age, sex, bmi, smoker, children, region]])
        predicted_expense = round(pred[0], 2)  # Round for better display

        # Pass the predicted expense to the template
        context = {
            'output': predicted_expense
        }
        return render(request, 'prediction.html', context)

    else:
        return render(request, 'prediction.html')
