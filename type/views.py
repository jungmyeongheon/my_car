from django.http import HttpResponse
from django.template import loader
from type.models import Type
from rest_framework import viewsets
from type.serializers import TypeSerializer

# TypeViewSet(viewsets.ModelViewSet):
    # queryset = Type.objects.all()
    # serializer_class = TypeSerializerclass 

def types(request):
  mytypes = Type.objects.all().values()
  template = loader.get_template('all_type.html')
  context = {
    'mytypes': mytypes,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mytype = Type.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mytype': mytype,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())