from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from vpn_service.views import SiteDeleteView, SiteCreateView, SiteListView, handle_vpn_route

app_name = "vpn"

urlpatterns = [
    path('list', login_required(SiteListView.as_view()), name='list'),
    path('create', login_required(SiteCreateView.as_view()), name='create'),
    path('delete/<int:pk>', login_required(SiteDeleteView.as_view()), name='delete'),
    re_path('(?P<site_name>[\w\d\s]+)/(?P<site_url>https://.*)', login_required(handle_vpn_route))
]
