from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('main_app.urls')),
]
