from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from django.conf import settings

@csrf_exempt
def keycloak_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        KC_BASE_URL = settings.KEYCLOAK_URL
        
        token_url = f'{KC_BASE_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/token'
        data = {
            'client_id': settings.KEYCLOAK_CLIENT_ID,
            'client_secret': settings.KEYCLOAK_CLIENT_SECRET,
            'grant_type': 'password',
            'username': username,
            'password': password,
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        
        response = requests.post(token_url, data=data, headers=headers)
        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse(response.json(), status=response.status_code)
    return JsonResponse({'error': 'Invalid request'}, status=400)