# -*- coding: utf-8 -*-
from django import forms


class MyContactForm(forms.Form):

    sender = forms.EmailField(label='Ваш email')
    subject = forms.CharField(label='Тема', max_length=100)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)
