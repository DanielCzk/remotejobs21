import django_filters
from job_form.models import Offer


class JobFilter(django_filters.FilterSet):

	title = django_filters.CharFilter(lookup_expr='icontains', label='')

	class Meta:

		model = Offer
		fields = ('title','experience_type', 'area_type',)
	

