# -*- coding: utf-8 -*-
from django import forms


class MyContactForm(forms.Form):

    user = forms.CharField(label='Имя', max_length=50)
    sender = forms.EmailField(label='Ваш email')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)

    # user = forms.CharField(label='Имя', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # sender = forms.EmailField(label='Ваш email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'form-control'}))


