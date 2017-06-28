from django.conf.urls import url

from . import views

app_name = 'sms'
urlpatterns = [
    url(r'^$', views.sms_send, name='sms_send'),
]
