from django import forms

class ContactForm(forms.Form):
    title = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    CHOICES = [('Memes','Processors'),
                ('GPUS','RAM')]
    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    subject = forms.CharField(required=True)
    body = forms.CharField(widget=forms.Textarea)
