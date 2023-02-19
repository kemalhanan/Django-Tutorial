from django.urls import path
from money_tracker.views import show_tracker

app_name = 'money_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
]
