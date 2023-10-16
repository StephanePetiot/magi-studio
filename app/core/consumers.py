# from channels.generic.websocket import AsyncWebsocketConsumer


# class ProcessingConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.channel_layer.group_add(f"processing-{self.scope['url_route']['kwargs']['id']}", self.channel_name)
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             f"processing-{self.scope['url_route']['kwargs']['id']}", self.channel_name
#         )

#     async def processing_message(self, event):
#         await self.send(self.channel_name, {"type": "processing_message", "message": event["text"]})
