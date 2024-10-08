from channels.generic.websocket import AsyncWebsocketConsumer
import json


class MessagesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        sender = self.scope["user"]
        recipient = data['recipient']

        # Check that the recipient is valid and exists
        if not recipient or not Recipient.objects.filter(id=recipient).exists():
            return

        # Create a new message
        msg = Message(sender=sender, recipient=recipient, message=data['message'])
        msg.save()

        # Send notification to recipient via websocket
        await self.send(text_data=json.dumps({
            'action': 'message_received',
            'message': data['message'],
        }))

    async def disconnect(self, close_code):
        pass