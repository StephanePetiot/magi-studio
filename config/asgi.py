import os

from django.core.asgi import get_asgi_application
asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from app.core.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.django.base")

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": asgi_app,

    # WebSocket handler
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})