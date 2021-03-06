from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from search import views as search_views
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from likes.views import save_like
from resources.views import get_json_data, get_location
from home.views import landing_page_controller
from resources.views import (
    assessment_controller, assessment_summary_controller
)

from cms.views import robots_handler

from wagtail.contrib.wagtailsitemaps.views import sitemap


handler404 = 'cms.views.not_found_handler'

urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url('^sitemap\.xml$', sitemap),

    url(r'^search/$', search_views.search, name='search'),

    url(r'^like/', save_like),

    url(r'^get_json_data/', get_json_data),

    url(r'^location/', get_location),

    url(
        r'^robots\.txt',
        robots_handler
    ),


    url('server-assessment/', assessment_controller),
    url('assessment-summary/', assessment_summary_controller),
    url(r'^sleep/', landing_page_controller),
    url('sleep/tips/', landing_page_controller),
    url('events/grenfell/', landing_page_controller),
    url('sleep-and-stress/', landing_page_controller),
    url('sleep-and-mind-racing/', landing_page_controller),
    url('sleep/talk-about-it/', landing_page_controller),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
