from django import forms

class ContactForm(forms.Form):
    title = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    CHOICES = [('Memes','Memes'),
                ('Processors','Processors'),
                ('Gpus', 'GPUS'),
                ('RAM','Ram'),
                ('Monitor','Monitor')]
    Category = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    Starting_Bid = forms.CharField(required=True)
    Description = forms.CharField(widget=forms.Textarea)
