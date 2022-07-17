from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    cc = forms.EmailField(required=False)
    bcc = forms.EmailField(required=False)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    file = forms.FileField(widget=forms.ClearableFileInput(), required=False)