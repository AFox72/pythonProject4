application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            url(r'^ws/message/(?P<recipient>\w+)/$', MessagesConsumer),
        ])
    ),
})
