from django.contrib import admin
from django.urls import re_path, path, include
from django.views.generic import RedirectView




urlpatterns_admin = [
    path('admin/', admin.site.urls),
]


urlpatterns_auth = [
    re_path(r'^accounts/', include('allauth.urls')),
]


urlpatterns = [
    path(
        '',
        RedirectView.as_view(pattern_name='account_signup'),
        name='default'
    )
]
urlpatterns.extend(urlpatterns_admin)
urlpatterns.extend(urlpatterns_auth)
