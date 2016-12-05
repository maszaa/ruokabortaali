from django.conf.urls import include, url
from django.contrib import admin
from api.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/$', DayMenuView.as_view()),
    url(r'^api/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/(?P<restaurant>\w{6,8})/$', RestaurantMenuView.as_view()),
    url(r'^api/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{1,2})/(?P<restaurant>\w{6,8})/(?P<menuName>\w+)/$', RestaurantOneMenuView.as_view()),
]
