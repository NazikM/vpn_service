from django.forms import ModelForm, TextInput

from vpn_service.models import Site


class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = '__all__'
