from django.conf.urls import url,include
from haystack.views import SearchView,search_view_factory
from .forms import TitleSearchForm
urlpatterns = [
    url(r'search/', search_view_factory(view_class = SearchView, form_class = TitleSearchForm), name='haystack_search'),
]