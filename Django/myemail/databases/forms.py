from django import forms
from databases.models import Header, Footer


class ContactForm(forms.Form):
    email_to = forms.EmailField(required=True)
    cc = forms.EmailField(required=False)
    bcc = forms.EmailField(required=False)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    file = forms.FileField(widget=forms.ClearableFileInput(), required=False)
    header = forms.ModelChoiceField(queryset=Header.objects.all(), required=False)
    footer = forms.ModelChoiceField(queryset=Footer.objects.all(), required=False)