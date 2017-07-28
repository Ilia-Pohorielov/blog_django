from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^admin_account/$', views.admin_account, name='admin_account'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/comment_create/$', views.comment_create, name='comment_create'),
    url(r'^post/(?P<pk>[0-9]+)/post_delete/$', views.post_delete, name='post_delete'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.update_profile, name='update_profile'),
    url(r'^post/(?P<pk>\d+)/favorite/$', views.add_remove_bookmark, name='add_remove_bookmark'),
]
