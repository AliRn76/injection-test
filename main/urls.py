from django.http import HttpResponse
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('user.urls', namespace='login_register'), name='root'),

    re_path(r'^.*$', lambda _: HttpResponse(status=404))
]

