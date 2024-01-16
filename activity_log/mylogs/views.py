from django.shortcuts import render

from .models import Activity

# Create your views here.
def index(request):
  context = {
    'activity': Activity.objects.all(),
  }
  return render(request=request, template_name="mylogs/index.html", context=context)