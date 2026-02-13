from django.urls import path
from . import views

app_name='yaziki'

urlpatterns = [
    path('prog_lang/', views.prog_lang_list_view, name='yaizki_programmirovanie'),
    path('prog_lang/<int:id>/', views.prog_lang_detail_view),
    path('prog_lang/<int:id>/delete/', views.delete_prog_lang_view),
    path('prog_lang/<int:id>/update/', views.update_proglang_view),

    path("create_prog_lang/", views.create_prog_lang_view, name='sozdat_blog'),

    path('search/', views.search_view),
]