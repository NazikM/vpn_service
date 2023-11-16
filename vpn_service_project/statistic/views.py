from django.views.generic import ListView

from statistic.models import VPNStatistic


class StatView(ListView):
    model = VPNStatistic
    fields = "__all__"
    template_name = 'statistic/statistic.html'
