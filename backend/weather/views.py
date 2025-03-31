import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view

API_KEY = "73d422b94361b85afeec276783143fe7"


@api_view(['GET'])
def get_weather(request):
    city = request.GET.get('city')
    if not city:
        return Response({'error': 'City not provided'}, status=400)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        return Response({'error': 'City not found'}, status=404)

    return Response(response.json())
