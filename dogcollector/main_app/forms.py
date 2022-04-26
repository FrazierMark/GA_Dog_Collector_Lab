from django.forms import ModelForm
from .models import Feeding

# purpose of this is to generate a form to later inject into the details page

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']