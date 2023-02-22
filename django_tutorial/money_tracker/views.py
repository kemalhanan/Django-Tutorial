from django.shortcuts import render
from django.shortcuts import render
from money_tracker.models import TransactionRecord
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_tracker(request):
    transaction_data = TransactionRecord.objects.all()
    context = {
    'list_of_transactions': transaction_data,
    'name': 'Kak Athal'
    }
    return render(request, "tracker.html", context)

def show_xml(request):
    data = TransactionRecord.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = TransactionRecord.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = TransactionRecord.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = TransactionRecord.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
