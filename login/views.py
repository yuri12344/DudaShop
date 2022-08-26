import json
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.middleware.csrf import get_token



def get_csrf(request):
    response = JsonResponse({"Info": "Success - Set CSRF cookie"})
    response["X-CSRFToken"] = get_token(request)
    return response


@require_POST
def loginView(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    if username is None or password is None:
        return JsonResponse({"info": "Username and Password is needed"})

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"info": "User does not exist"}, status=400)

    login(request, user)
    request.session.create()
    return JsonResponse({"info": "User logged in successfully"})

