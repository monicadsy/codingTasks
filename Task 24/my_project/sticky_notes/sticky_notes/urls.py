"""
URL configuration for sticky_notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import note_list, note_detail, note_create, note_update, note_delete

urlpatterns = [
    # URL pattern for displaying a list of all notes
    path('', note_list, name='note_list'),

    # URL pattern for displaying details of a specific note
    path('note/<int:pk>/', note_detail, name='note_detail'),

    # URL pattern for creating a new note
    path('note/new/', note_create, name='note_create'),

    # URL pattern for displaying details of a specific note
    path('note/<int:pk>/edit/', note_update, name='note_upate'),

        # URL pattern for displaying details of a specific note
    path('note/<int:pk>/delete/', note_delete, name='note_delete'),
]

# bulletin_board/urls.py
from django.contrib import admin
from django.urls import path, include

# Define URL patterns for the entire project
urlpatterns = [
    # Admin URL pattern, mapping to the Django admin interface
    path('admin/', admin.site.urls),

    # inlcude URL patterns from the 'notes' app
    # All URLs from 'notes.urls' will be prefixed with 'notes/'
    path('', include('notes.urls')),
]