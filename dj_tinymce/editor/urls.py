from django.urls import path
# import local views
from . import views

urlpatterns = [
    # editor/
    path(r'', views.index, name='index-name'), 

    # editor/808244750988245/
    path(r'<int:editor_id>/', views.nth_editor, name='edito_nth'),

    # editor/808244750988245/ajax/submit_html
    path(r'<int:editor_id>/ajax/submit_html/', views.save_nth_editor, name='edito_nth_save'),

    # editor/808244750988245/view_nth
    path(r'<int:editor_id>/view_nth/', views.view_nth_page, name='view nth page')]
