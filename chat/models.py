from datetime import date, datetime
from django.conf import settings
from django.db import models

# Create your models here.
class Chat(models.Model):
    created_at = models.DateField(default=date.today)

class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    time = models.TimeField(default=datetime.now)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, blank=True, null=True)
    # default= None bedeutet wenn nichts geschrieben wird kommt nichts rein, ansonsten würde es nicht funktionieren
    # blank=True wird gesetzt um es zu erlauben das nichts gesendet werden darf
    # null= True damit sagen wir der Datenbank das sie nicht aktzeptieren darf

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set') 
    # mit ForeignKey wird das Objekt referenziert in dem Fall der Author
    # on delete=models.CASCADE muss gesetzt werden damit Nachrichten auch gelöscht werden wenn der User gelöscht wird. related_name
    # wird für die Datenbank gebraucht, Sie verknüpft die Message mit dem Author

    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')

