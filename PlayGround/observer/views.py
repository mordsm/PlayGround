from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,DetailView,ListView
from .forms import TemplateForm
from .models import ActiveData,DataTemplate,Data
# ...
def detail(request, data_id):
    data = get_object_or_404(ActiveData, pk=data_id)
    return render(request, 'detail.html', {'data': data})


def template(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TemplateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = \
            TemplateForm()

    return render(request, 'template.html', {'form': form})

class AddTemplateView(CreateView):
    model = DataTemplate
    form_class = TemplateForm
    template_name = "template.html"