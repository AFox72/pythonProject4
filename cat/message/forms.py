from django import forms

class MessageForm(forms.Form):
    recipient = forms.CharField(label='Получатель')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')