from django.urls import path
# import local views
from . import views

urlpatterns = [
    # editor/
    path(r'', views.index, name='index-name'), 

    # editor/808244750988245/
    path(r'<int:editor_id>/', views.nth_editor, name='edito_nth'),

]
