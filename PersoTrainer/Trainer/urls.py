from django.conf.urls import url
from . import views_act, views_myAct, views, views_chat

urlpatterns = [

    url(r'^activities/$', views_act.activities, name = 'activities'),
    url(r'^activities/detail/(?P<activity_pk>\d+)/$', views_act.activity_detail, name='activity_detail'),
    url(r'^add_act$', views_act.add_act, name = 'add_act'),

    url(r'^MyActivities/$', views_myAct.MyActivities, name = 'MyActivities'),

    url(r'^chatRoom/$', views_chat.index, name='index'),
    # url(r'^(?P<chat_room_id>\d+)/$', views_chat.chat_room, name='chat_room'),


    url(r'^post/$', views_chat.Post, name='post'),
    url(r'^chat_room/$', views_chat.chat_room, name='chat_room'),

]
