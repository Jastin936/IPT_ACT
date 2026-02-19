from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('records.urls')), # This connects your app
    path('', RedirectView.as_view(url='show/')),
]