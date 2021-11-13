from django.http import JsonResponse
from .models import Client


# Function Based View
def json_view(request):
    # getting data from models and returning in json format
    clients = Client.objects.all()
    data = [client.to_dict_json() for client in clients]
    response = {'data': data}
    return JsonResponse(response)
