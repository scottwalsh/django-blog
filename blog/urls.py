from django.conf.urls.defaults import * 
from blog.models import Entry  
from tagging.views import tagged_object_list 
   
info_dict = {
	'queryset': Entry.objects.filter(status=1),
	'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
	(r'^$','archive_index', dict(info_dict, template_name='blog/archive.html')),
	(r'^(?P<year>\d{4})/$','archive_year', dict(info_dict, make_object_list=True, template_name='blog/archive_year.html')),
	(r'^(?P<year>\d{4})/(?P<month>\w{3})/$','archive_month', dict(info_dict, template_name='blog/archive_month.html')),
	(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$','archive_day',dict(info_dict, template_name='blog/archive_day.html')),
	(r'(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\d\w]+)/$', 'object_detail', dict(info_dict, slug_field='slug', template_name='blog/detail.html')),
)
