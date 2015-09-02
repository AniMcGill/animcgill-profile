from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.template import RequestContext
from aniprofile.models import Profile, Exec
from aniprofile.forms import RegistrationForm
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib import messages

# Create your views here.


class ProfileView(DetailView):
    model = Profile
    template_name = "aniprofile/profile.html"
    context_object_name = "usr"

    def get_object(self, queryset=Profile):
        try:
            pk = self.kwargs["pk"]
            o = get_object_or_404(queryset, pk)
        except:
            if self.request.user.is_authenticated:
                o = self.request.user
            else:
                raise PermissionDenied
        return o


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid() and form.cleaned_data['test'].upper() == "MCGILL":
            password = form.cleaned_data['password']
            if form.cleaned_data['passwordConfirm'] != password:
                return render_to_response('accounts/register.html', {'form': form},
                    context_instance=RequestContext(request))
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.save()
            user.profile.save()
            messages.add_message(request, messages.SUCCESS, 'Registration Complete')
            return HttpResponseRedirect('/accounts/login/')
        else:
            messages.add_message(request, messages.ERROR, 'Registration error')
            return render_to_response('accounts/register.html', {'form': form},
                context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
        return render_to_response('accounts/register.html', {'form': form},
            context_instance=RequestContext(request))


class ExecList(ListView):
    queryset = Exec.objects.filter(active=True)
    template_name = "aniprofile/execs.html"
    context_object_name = "execs"