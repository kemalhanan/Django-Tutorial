from django.shortcuts import render
from django.shortcuts import render
from money_tracker.models import TransactionRecord

# Create your views here.
def show_tracker(request):
    transaction_data = TransactionRecord.objects.all()
    context = {
    'list_of_transactions': transaction_data,
    'name': 'Kak Athal'
    }
    return render(request, "tracker.html", context)
