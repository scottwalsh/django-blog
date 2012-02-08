from django.conf.urls.defaults import *

from django.contrib import admin

from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^djangoblog/', include('djangoblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

	(r'^admin/(.*)', admin.site.root),
	(r'^blog/', include('djangoblog.blog.urls')),
	(r'^blog/tags/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'djangoblog.tag_views.tag_detail'),
	(r'^blog/tags/', 'djangoblog.tag_views.all_tags'),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
