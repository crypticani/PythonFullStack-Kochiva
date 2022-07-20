from django import forms


class WeatherForm(forms.Form):
    search_box = forms.CharField(required=True, widget=forms.TextInput(attrs={'id':'search'}))