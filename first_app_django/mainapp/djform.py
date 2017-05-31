# -*- coding: utf-8 -*-
from django import forms


class MyContactForm(forms.Form):

    sender = forms.EmailField(label='Ваш email')
    subject = forms.CharField(label='Тема', max_length=100)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)


    # user = forms.CharField(label='Имя', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # sender = forms.EmailField(label='Ваш email', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    # subject = forms.CharField(label='Тема', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    # message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class' : 'form-control'}))
