from django import forms
from .models import Listing
Categories_Available = [('Memes','Memes'),
                        ('Processors','Processors'),
                        ('Gpus', 'GPUS'),
                        ('RAM','Ram'),
                        ('Monitor','Monitor')]
class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title','author','Starting_Bid','Description','Category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control-sm'}),
            'Starting_Bid': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'Description': forms.Textarea(attrs={'class': 'form-control-sm'}),
            'Category': forms.RadioSelect(attrs={'class': 'form-control-sm'}, choices=Categories_Available),

        }
