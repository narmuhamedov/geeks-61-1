from django.urls import path
from . import views

urlpatterns = [
    path('prog_lang/', views.prog_lang_list_view),
    path('prog_lang/<int:id>/', views.prog_lang_detail_view),
    path('prog_lang/<int:id>/delete/', views.delete_prog_lang_view),
    path('prog_lang/<int:id>/update/', views.update_proglang_view),

    path("create_prog_lang/", views.create_prog_lang_view),
]