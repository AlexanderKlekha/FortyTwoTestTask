from django.views.generic import ListView
from models import Person

# Create your views here.


class PersonIndexView(ListView):
    template_name = 'person/index.html'
    model = Person
