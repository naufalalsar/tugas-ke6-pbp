# TODO: Implement Routings Here

from django.urls import path
from mywatchlist.views import *

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_html, name='show_html'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
]
