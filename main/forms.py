from django.forms import ModelForm
from main.models import Entry

class OrderEntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [ 'item_name', 'price', 'description', 'rating']