from email.mime import application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from  .import consumers

websocket_urlpatterns = [
    #re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi())
    re_path(r"ws/chat/(?P<chat_box_name>\w+)/$", consumers.ChatConsumer.as_asgi() ),
]

application = ProtocolTypeRouter( 
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)