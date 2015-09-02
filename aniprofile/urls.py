from django.conf.urls import patterns, include, url
from aniprofile.views import ProfileView

urlpatterns = patterns('',
    url(r'^profile/$', ProfileView.as_view(), name="self_user_view"),
    url(r'^profile/(?P<pk>\d+)/$', ProfileView.as_view(), name="user_view"),
    #url(r'^register/$','MAC_profile.views.registration',name="register"),
    url('^', include('django.contrib.auth.urls'))
)
