from django.views.generic import CreateView

from .models import SPSElement
from .forms import SPSElementForm


class SPSElementCreateView(CreateView):
    model = SPSElement
    form_class = SPSElementForm
