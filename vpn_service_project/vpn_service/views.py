import re
from wsgiref.util import is_hop_by_hop

import requests
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from vpn_service.forms import SiteForm
from vpn_service.models import Site


class SiteListView(ListView):
    template_name = 'vpn_service/list_sites.html'
    model = Site
    fields = '__all__'
    # paginate_by = 3


class SiteCreateView(CreateView):
    model = Site
    fields = ['name', 'url']
    template_name = 'vpn_service/create_site.html'
    success_url = reverse_lazy('vpn:create')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SiteDeleteView(DeleteView):
    model = Site
    success_url = reverse_lazy('vpn:list')


def replace_links(html_content, site_name, site_url):
    authority = re.search('https?://[^\s/]+', site_url).group(0)

    # Define the pattern to match YouTube links
    pattern_single = re.compile(f'href=\'{authority}/')
    pattern_double = re.compile(f'href=\"{authority}/')
    # Replace YouTube links with the specified format
    modified_content = pattern_single.sub(f'href=\'localhost:8000/{site_name}/{authority}/', html_content)
    modified_content = pattern_double.sub(f'href=\"localhost:8000/{site_name}/{authority}/', modified_content)

    return modified_content.encode('utf-8')


def format_response(html_content, status, cookies):
    # headers = {key: value for key, value in response.headers.items() if not is_hop_by_hop(key)}
    http_response = HttpResponse(html_content,
                                 # headers=headers,
                                 status=status)
    for cookie in cookies:
        http_response.set_cookie(key=cookie.name, value=cookie.value, expires=cookie.expires,
                                 path=cookie.path, domain=cookie.domain,
                                 secure=cookie.secure)
    return http_response


def handle_vpn_route(request, site_name, site_url):
    if request.method == "GET":
        response = requests.get(site_url, cookies=request.COOKIES)
        html_content = replace_links(response.content.decode('utf-8'), site_name, site_url)
        return format_response(html_content, response.status_code, response.cookies)
    elif request.method == "POST":
        response = requests.post(site_url, data=request.body, cookies=request.COOKIES)
        return format_response(response.content, response.status_code, response.cookies)
