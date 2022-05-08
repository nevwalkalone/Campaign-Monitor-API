from django import forms


class SubscriberForm(forms.Form):
    full_name = forms.CharField(max_length=250)
    email = forms.EmailField()
