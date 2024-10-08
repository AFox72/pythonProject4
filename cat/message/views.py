import json

from django.shortcuts import render, redirect

from .models import Message


def messages_page(request):
    messages = Message.objects.all()
    context = {
        'message': messages,
    }
    return render(request, 'message.html', context)


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']

            # Use websockets to notify recipient of new message
            connection = WebsocketConnection.get_connection(recipient)
            if connection:
                connection.send(json.dumps({
                    'action': 'new_message',
                    'message': form.cleaned_data['message'],
                }))

            return redirect('message')
    else:
        form = MessageForm()
    context = {'form': form}
    return render(request, 'send_message.html', context)