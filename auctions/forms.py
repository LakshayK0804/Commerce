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
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title of your listing', 'required': 'required'}),
            'author': forms.Select(attrs={'class': 'form-control-sm', 'placeholder': 'Your username', 'required': 'required'}),
            'Starting_Bid': forms.NumberInput(attrs={'class': 'form-control-sm','placeholder': 'The starting bid of your listing', 'required': 'required'}),
            'Description': forms.Textarea(attrs={'class': 'form-control-sm','placeholder': 'Describe your listing', 'required': 'required'}),
            'Category': forms.RadioSelect(attrs={'class': 'form-control-sm', 'placeholder': 'Select a category', 'required': 'required'}, choices=Categories_Available),
            'Closedlisting': forms.TextInput(attrs={'class': 'form-control'})
        }

class EditedListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('Closedlisting',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title of your listing', 'disabled': 'disabled'}),
            'author': forms.Select(attrs={'class': 'form-control-sm', 'placeholder': 'Your username', 'disabled': 'disabled'}),
            'Starting_Bid': forms.NumberInput(attrs={'class': 'form-control-sm','placeholder': 'The starting bid of your listing', 'disabled': 'disabled'}),
            'Description': forms.Textarea(attrs={'class': 'form-control-sm','placeholder': 'Describe your listing', 'disabled': 'disabled'}),
            'Category': forms.RadioSelect(attrs={'class': 'form-control-sm', 'placeholder': 'Select a category', 'disabled': 'disabled'}, choices=Categories_Available),
            'Closedlisting': forms.TextInput(attrs={'class': 'form-control', 'value':'This listing is now closed', })
        }
