from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Vet,Surgery,Animal
from django.shortcuts import render

# # Create your views here.
class VetListView(ListView):
    model = Vet
    template_name = 'vlist.html'
    context_object_name = 'all_vets_list'

class VetDetailView(DetailView):
    model = Vet
    template_name = 'v_detail.html'

class VetCreateView(CreateView):
    model = Vet
    template_name = 'v_create.html'
    fields = ['name', 'years_experience', 'animals','surgery']

class VetUpdateView(UpdateView):
    model = Vet
    template_name = 'v_edit.html'
    fields = ['animals']

class SVListView(ListView):
    model = Surgery
    template_name = 'sv_list.html'
    context_object_name = 'all_s_list'

def query1(request):
    # Initialize an empty context to pass to the template
    context = {
        'num_dogs': None,
        'error_message': None,
    }

    try:
        number = Animal.objects.filter(species="Dog").count()
        context['num_dogs'] = number
      
    except Animal.DoesNotExist:
        context['error_message'] = "No animals found."
    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query1.html', context)


def query2(request):
    # Initialize an empty context to pass to the template
    context = {
        'name':None,
        'num_vets': None,
        'error_message': None,
    }

    try:
        happy_surgery = Surgery.objects.get(name="Happy Paws Surgery Center")
        number = Vet.objects.filter(surgery=happy_surgery).count()
        context['num_vets'] = number
        context['name'] = happy_surgery.name

    except Surgery.DoesNotExist:
        context['error_message'] = "No surgery found."
    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query2.html', context)


