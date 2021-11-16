from django.http import JsonResponse
from .models import Client
from .forms import ClientForm
from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy


# Function Based View
def json_view(request):
    # getting data from models and returning in json format
    clients = Client.objects.all()
    data = [client.to_dict_json() for client in clients]
    response = {'data': data}
    return JsonResponse(response)


# Class Based Views
class IndexFormView(FormView):
    template_name = 'core/index.html'
    form_class = ClientForm
    success_url = reverse_lazy('core:json_view')

    def form_valid(self, form, *args, **kwargs):
        form.save()
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return super(IndexFormView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Ocorreu um erro. Verifique os dados informados!')
        return super(IndexFormView, self).form_invalid(form, *args, **kwargs)
