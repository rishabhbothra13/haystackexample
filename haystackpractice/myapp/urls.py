# from django.conf.urls import url,include
# from haystack.views import SearchView

# urlpatterns = [
#     url(r'^$', SearchView, name='haystack_search'),
# ]

from django.conf.urls import url
from haystack.forms import FacetedSearchForm
from .views import FacetedSearchView

urlpatterns = [
url(r'^$', FacetedSearchView.as_view(), name='haystack_search'),
]