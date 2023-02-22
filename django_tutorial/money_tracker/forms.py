from django.forms import ModelForm
from money_tracker.models import TransactionRecord

class TransactionRecordForm(ModelForm):
    class Meta:
        model = TransactionRecord
        fields = ["name", "type", "amount", "description"]