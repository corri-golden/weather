from django.shortcuts import render


# Create your views here.

def home(request):
    import json
    # go and grab the api and bring the data back
    import requests
    #for search function
    if request.method == "POST":
        zipcode = request.POST['zipcode']
    
        # goes and grab the api
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=4F325584-8D86-4659-BF8E-44A252A8756B")

        try:
            
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        
        if api[0]['Category']['Name'] == "Good":  
            category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51-100) If you are unusually sensitive to particle pollution, consider reducing your activity level or shorten the amount of time you are active outdoors."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) Although general public is not likely to be affected at this AQI range, people with lung disease and the elder should take caution."
            category_color = "Unhealthy for Sensitive Groups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200) Everyone may begin to experience health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201-300) Health Alert: everyone may experience more serious health effects."
            category_color = "very unhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description ="(301-500) Health warnings of emergency conditions.  The entire population is more likely to be affected."
            category_color = "hazardous"

        



        return render(request, 'home.html', {'api': api, "category_description": category_description, "category_color": category_color})

    else:
        # goes and get the api
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=37207&distance=5&API_KEY=4F325584-8D86-4659-BF8E-44A252A8756B")

        try:
            
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        
        if api[0]['Category']['Name'] == "Good":  
            category_description = "(0-50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51-100) If you are unusually sensitive to particle pollution, consider reducing your activity level or shorten the amount of time you are active outdoors."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) Although general public is not likely to be affected at this AQI range, people with lung disease and the elder should take caution."
            category_color = "Unhealthy for Sensitive Groups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200) Everyone may begin to experience health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201-300) Health Alert: everyone may experience more serious health effects."
            category_color = "very unhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description ="(301-500) Health warnings of emergency conditions.  The entire population is more likely to be affected."
            category_color = "hazardous"

        



        return render(request, 'home.html', {'api': api, "category_description": category_description, "category_color": category_color})

def about(request):
    return render(request, 'about.html', {})
