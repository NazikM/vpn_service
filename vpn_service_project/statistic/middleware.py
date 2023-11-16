from vpn_service.models import Site
from .models import VPNStatistic


class VPNStatisticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    @staticmethod
    def calculate_headers_size(headers):
        size = 0
        for k, v in headers.items():
            size += len(k.encode('utf-8')) + len(k.encode('utf-8'))
        return size

    def process_view(self, request, view_func, view_args, view_kwargs):
        if 'site_name' in view_kwargs and 'site_url' in view_kwargs and request.user.is_authenticated:
            site = Site.objects.get(user=request.user, name=view_kwargs['site_name'])
            site_statistics, created = VPNStatistic.objects.get_or_create(site=site)

            site_statistics.transitions += 1
            headers_size = self.calculate_headers_size(request.headers)
            print(repr(request.META.get('CONTENT_LENGTH', 0)))
            site_statistics.uploaded_data += int(request.META.get('CONTENT_LENGTH', 0) or 0) + headers_size

            response = view_func(request, **view_kwargs)
            headers_size = self.calculate_headers_size(response.headers)
            print(type(response.content))
            site_statistics.downloaded_data += len(response.content) + headers_size
            site_statistics.save()

            return response
