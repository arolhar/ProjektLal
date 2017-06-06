from django.views import generic
from .models import Info


class InfoIndexView(generic.ListView):
    template_name = 'info_index.html'
    context_object_name = 'all_informations'

    def get_queryset(self):
        return Info.objects.all()

class InfoDetailView(generic.DetailView):
    model = Info
    template_name = 'info_detail.html'