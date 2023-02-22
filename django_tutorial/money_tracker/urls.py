from django.urls import path
from money_tracker.views import show_tracker
from money_tracker.views import show_xml
from money_tracker.views import show_json
from money_tracker.views import show_xml_by_id, show_json_by_id
from money_tracker.views import create_transaction

app_name = 'money_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('create', create_transaction, name='create_transaction'),
]
