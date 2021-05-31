from django.conf.urls import url
from .views import MeterView

urlpatterns = [
    url(r'^meter/$', MeterView.as_view(), name='meter')
]