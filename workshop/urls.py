from django.conf.urls import patterns, include, url
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from django.contrib import admin
from django.contrib.auth.decorators import login_required

import account.views
from customer.models import Customer


# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', account.views.index, name='index'),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}, name='login'),
	url(r'^logout/$', account.views.logout, name='logout'),
	url(r'^main/$', account.views.index, name='main'),
	url(r'^customers/$', 
		login_required(ListView.as_view(
			queryset=Customer.objects.order_by("name").all())), 
		name='customers'),
	url(r'^customers/new/$', 
		login_required(CreateView.as_view(
			model=Customer,
			success_url="/customers/%(id)s/")),
		name='new_customer'),
    # Examples:
    # url(r'^$', 'workshop.views.home', name='home'),
    # url(r'^workshop/', include('workshop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
