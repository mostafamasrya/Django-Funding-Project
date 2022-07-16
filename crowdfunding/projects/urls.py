
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', home, name = 'home'),
    path('add_project/', add_project, name = 'add_project'),
    path('admin/', admin_home, name = 'admin'),
    path('admin/add5projects/', add5projects, name = 'add5projects'),
    path('admin/project_reports/', project_reports, name = 'project_reports'),
    path('admin/comments_reports/', comments_reports, name = 'comments_reports'),
    path('list_projects/', list_projects, name = 'list_projects'),
    path('add_report/', add_report, name = 'add_report'),
    path('product_details/<id>', project_info, name = 'product_details'),
    path('add_rate/<id>', add_rate, name = 'add_rate'),
    path('add_comment/<id>', add_comment, name = 'add_comment'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)