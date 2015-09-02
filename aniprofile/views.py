from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from aniprofile.models import Profile, Exec
from django.core.exceptions import PermissionDenied

# Create your views here.


class ProfileView(DetailView):
    model = Profile
    template_name = "aniprofile/profile.html"
    context_object_name = "usr"

    def get_object(self, queryset=None):
        try:
            pk = self.kwargs["pk"]
        except:
            if self.request.user.is_authenticated:
                pk = self.request.user.id
            else:
                raise PermissionDenied
        o = get_object_or_404(queryset, pk)
        return o
