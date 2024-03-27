from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User

# Create your views here.
def home(request):
    return HttpResponse('Hello World!')

def addNumbers(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    result = val1 + val2
    return HttpResponse('Result: ' + str(result))

def viewUsers(request):
    # Get the queryset of User objects
    user_queryset = User.objects.all()
    # Convert the queryset to a list of dictionaries
    user_list = list(user_queryset.values())
    # Returning a JSON response
    return JsonResponse(user_list, safe=False)