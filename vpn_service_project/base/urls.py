from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from statistic.views import StatView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('user_management.urls', namespace="profile")),
    path('', include('vpn_service.urls', namespace="vpn")),
    path('stat/', login_required(StatView.as_view()), name='statistic')
]
