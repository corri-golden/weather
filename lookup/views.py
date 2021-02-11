from django.shortcuts import render


# Create your views here.

def home(request):
    import json
    # go and grab the api and bring the data back
    import requests

    # goes and grab the api
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=37207&distance=5&API_KEY=4F325584-8D86-4659-BF8E-44A252A8756B")

    try:
        
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."


    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
