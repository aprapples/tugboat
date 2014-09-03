from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from tool1.views import (Medications_Create, Patient_List, Medications_List, 
			 Medications_Update, Medications_Delete)
from tool1.views import search_form, search, upload_file


admin.autodiscover()

urlpatterns = patterns('',	
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^test/', TemplateView.as_view(template_name='test_datepicker.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', 
	{'template_name': 'login.html'}),
    url(r'^new/(?P<pk>\d+)/$', Medications_Create.as_view(), name='med_new'),
    url(r'^list/$', Patient_List.as_view(), name='search_form'),
    url(r'^med_list/', Medications_List.as_view(), name='med_list'),	
    url(r'^edit/(?P<pk>\d+)/$', Medications_Update.as_view(), name='med_edit'),
#    url(r'^search_form/$', search_form),
    url(r'^upload/$', upload_file),
    url(r'^search/$', search),
#    url(r'^search/$', Patient_Search.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', Medications_Delete.as_view(),name='med_delete'),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
