from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import ChatRoom

def index(request):
  c = ChatRoom.objects.all()
  return render(request, "chat/index.html", {'home': 'active', 'chat': c})

# def chat_room(request, chat_room_id):
#   chat = get_object_or_404(ChatRoom, pk=chat_room_id)
#   return render(request, 'chat/chat_room.html', {'chat': chat})


# def Home(request):
#     c = Chat.objects.all()
#     return render(request, "chat/index.html", {'home': 'active', 'chat': c})

def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = ChatRoom(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

def chat_room(request):
    c = ChatRoom.objects.all()
    return render(request, 'chat/messages.html', {'chat': c})
