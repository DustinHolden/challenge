from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic.base import TemplateView


# This is just boilerplate to give us a landing page to view.
class HomeView(TemplateView):
    template_name = 'index.html'


urlpatterns = [
                  path('', HomeView.as_view(), name='home'),
                  # Django Admin, use {% url 'admin:index' %}
                  path(settings.ADMIN_URL, admin.site.urls),
                  # User management
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path('api/', include('config.api_router')),
    # API login
    path('api-auth/', include('rest_framework.urls')),
    # API Token and Registration
    path('auth-token/', obtain_auth_token, name='get-auth-token'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            '400/',
            default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')},
        ),
        path(
            '403/',
            default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')},
        ),
        path(
            '404/',
            default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')},
        ),
        path('500/', default_views.server_error),
    ]
