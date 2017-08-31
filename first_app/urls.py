from django.conf.urls import url
from first_app import views

# for TEMPLATE TAGGING, Django always look for app_name global variable. Used here in case for a href . <a href="{% url 'first_app:other' %}">The OTHER Page</a>
app_name = 'first_app'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$',views.user_logout,name='user_logout'),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^cbv/$',views.TemplateViewClass.as_view()),
    url(r'^list/$',views.TopicListView.as_view(),name='list'),
    url(r'^list/(?P<pk>\d+)/$',views.TopicDetailView.as_view(),name='detail'),
    url(r'^create/$',views.TopicCreateView.as_view(),name='create'),
    url(r'^list/update/(?P<pk>\d+)/$',views.TopicUpdateView.as_view(),name='update'),
    url(r'^list/delete/(?P<pk>\d+)/$',views.TopicDeleteView.as_view(),name='delete'),





]
