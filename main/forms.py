from django.forms import ModelForm
from main.models import Entry
from django.utils.html import strip_tags

class OrderEntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [ 'item_name', 'price', 'description', 'rating']

    def clean_item_name(self):
        item_name = self.cleaned_data["item_name"]
        return strip_tags(item_name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)