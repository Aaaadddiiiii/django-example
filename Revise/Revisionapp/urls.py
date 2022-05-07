from django.conf.urls import url
from Revisionapp import views

# TEMPLATE TAGGING
app_name = 'Revisionapp'


urlpatterns = [
    url(r'^formpage/',views.formpage,name='formpage'),
    url(r'^signup/',views.usersignup,name='usersignup'),
    url(r'^register/',views.register,name='register'),
    url(r'^user_login/',views.user_login,name='user_login'),
]
