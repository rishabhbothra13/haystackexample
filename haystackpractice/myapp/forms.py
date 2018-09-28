from django import forms
from haystack.forms import SearchForm


class TitleSearchForm(SearchForm):
    title = forms.CharField(required=False)

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(TitleSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        # Check to see if a start_date was chosen.
        if self.cleaned_data['title']:
            sqs = sqs.filter(title=self.cleaned_data['title'])

        # Check to see if an end_date was chosen.

        return sqs
