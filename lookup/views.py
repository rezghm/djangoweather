from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=89129&date=2025-07-08&distance=5&API_KEY=2764329E-90D0-43B0-B945-3D247C4175E2")
	try:
		api = json.loads(api_request.content)

	except Exception as e:
		api = "Error..."

	return render(request, 'home.html', {'api': api})

def about(request):
	return render(request, 'about.html', {})