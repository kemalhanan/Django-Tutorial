from django.shortcuts import render
from django.shortcuts import render
from money_tracker.models import TransactionRecord
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from money_tracker.forms import TransactionRecordForm
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def show_tracker(request):
    transaction_data = TransactionRecord.objects.all()
    context = {
    'list_of_transactions': transaction_data,
    'name': request.user.username,
    }
    return render(request, "tracker.html", context)

def create_transaction(request):
    form = TransactionRecordForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('money_tracker:show_tracker'))

    context = {'form': form}
    return render(request, "create_transaction.html", context)

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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('money_tracker:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('money_tracker:show_tracker')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)