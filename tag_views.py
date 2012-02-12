from django.views.generic.list_detail import object_list
from tagging.models import Tag,TaggedItem
from blog.models import Entry

def tag_detail(request, slug):
	unslug = slug.replace('-', ' ')
	tag = Tag.objects.get(name=unslug)
	qs = TaggedItem.objects.get_by_model(Entry, tag)
	return object_list(request, queryset=qs, extra_context={'tag':slug}, template_name='tags/detail.html')

# This function appears not to be working correctly in pdb.. template not shown
# Potential causes include; bad return format, bad template format, maybe more
def all_tags(request):
	qs = Tag.objects.all()
	return object_list(request, queryset=qs, template_name='tags/list.html')
