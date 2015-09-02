from django.conf.urls import patterns, include, url
from aniprofile.views import ProfileView, ExecList

urlpatterns = patterns('',
    url(r'^profile/$', ProfileView.as_view(), name="self_user_view"),
    url(r'^profile/(?P<pk>\d+)/$', ProfileView.as_view(), name="user_view"),
    url(r'^register/$', 'aniprofile.views.registration', name="register"),
    url(r'^execs/$', ExecList.as_view(), name="exec_list"),
    url('^', include('django.contrib.auth.urls'))
)
