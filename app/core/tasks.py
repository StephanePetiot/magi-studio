# from asgiref.sync import async_to_sync
# from celery import shared_task
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


async def closing_send(channel_layer, channel, message):
    await channel_layer.group_send(channel, message)
    await channel_layer.close_pools()
