from django.shortcuts import render
from .models import Chat, Message
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model



@login_required(login_url='login/')
def chat(request):
    if request.method == 'POST':  
        print("Received data" + request.POST['textmessage'])
        # Hier wird der aktuelle Chat, in diesem Fall mit der id=1 einer Variablen übergeben
        myChat = Chat.objects.get(id=1)
        # Hier wird das Message Object erstellt, der text kommt aus der Textmessage und dann wird noch chat, author und receiver hinzugefügt
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        serialized_obj = serializers.serialize('json', [new_message,])
        return JsonResponse(serialized_obj[1:-1], safe=False)
        

    allChatMessages = Message.objects.filter(chat__id=1)  # Filter nach eigenen Nachrichten
    register_users = get_user_model().objects.all()
    return render(request, 'chat.html', {'allMessages': allChatMessages, 'register_users' : register_users})
    # messages : chatMessages gibt die Nachrichten wieder, diese kann ich dann im HTML darstellen



