from django.views.generic import DetailView, ListView
from tender.models import Tender


class TenderListView(ListView):
    model = Tender


class TenderDetailView(DetailView):
    model = Tender
    context_object_name = "tender"



