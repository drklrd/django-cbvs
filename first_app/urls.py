from django.conf.urls import url
from first_app import views

# for TEMPLATE TAGGING, Django always look for app_name global varialble. Used here in case for a href . <a href="{% url 'first_app:other' %}">The OTHER Page</a>
app_name = 'first_app'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other')
]
