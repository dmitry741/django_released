# -*- coding: utf-8 -*-
from django import forms


class MyContactForm(forms.Form):
    # sender = forms.EmailField(label='Ваш email')
    sender = forms.EmailField(label='Ваш email', widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Ваш Email'}))
    subject = forms.CharField(label='Тема', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Тема'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Сообщение'}))
