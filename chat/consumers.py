import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat.name = self.scope["url_route"]["kwargs"]["chat.name"]
        self.group_name = "chat_%s" % self.chat.name

        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    
    #     self.room_group_name = 'Chatroom 1'

    #     #async_to_sync(self.channel_layer.group_add)(
    #     await self.channel_layer.group_add(
    #         self.room_group_name,
    #         self.channel_name
    #     )

    #    self.accect()



    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json["username"]

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": username,
            },
        )
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,
        #     {
        #         'type':'chat_message',
        #         'message':message
        #     }
        # )

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]

        await self.send(text_data=json.dumps({
            "message": message,
            "username": username,
        }))
  