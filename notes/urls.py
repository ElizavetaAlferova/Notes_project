from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexListView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
    path('notes/<int:pk>/', views.notes_detail, name='note_detail'),
    path('pdf/<int:pk>/', views.pdf_view, name='pdf_view'),
    path('upload/', views.create_notes, name='upload'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete')
]