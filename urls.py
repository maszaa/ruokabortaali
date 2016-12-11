from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView
from api.views import *
from client.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/$', TemplateView.as_view(template_name='apidokumentaatio.html')),
    url(r'^api/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', DayMenuView.as_view()),
    url(r'^api/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<restaurant>\w{6,8})/$', RestaurantMenuView.as_view()),
    url(r'^api/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<restaurant>\w{6,8})/(?P<menuName>.*)/$', RestaurantOneMenuView.as_view()),

    url(r'^$', TemplateView.as_view(template_name='ruokabortaali.html')),
    url(r'^test/$', TemplateView.as_view(template_name='test.html')),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
]
