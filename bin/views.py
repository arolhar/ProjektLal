#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from accounts.models import UserProfile
from web.models import Info, News, Pack, Equipment
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['last_info'] = Info.objects.all().order_by('-id')[:1]
        context['last_news'] = News.objects.all().order_by('-id')[:3]
        context['last_pack'] = Pack.objects.all().order_by('-id')[:3]
        context['last_equipment'] = Pack.objects.all().order_by('-id')[:5]
        context['last_user'] = User.objects.all().order_by('-id')[:4]
        return context