"""
URL configuration for gallery project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from galeria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Artist URLs
    path('artists/', views.ArtistListView.as_view(), name='artist_list'),
    path('artist/<int:pk>/detail/', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('artist/create/', views.ArtistCreateView.as_view(), name='artist_create'),
    path('artist/<int:pk>/update/', views.ArtistUpdateView.as_view(), name='artist_update'),
    path('artist/<int:pk>/delete/', views.ArtistDeleteView.as_view(), name='artist_delete'),

    # Artwork URLs
    path('artworks/', views.ArtworkListView.as_view(), name='artwork_list'),
    path('artwork/<int:pk>/detail/', views.ArtworkDetailView.as_view(), name='artwork_detail'),
    path('artwork/create/', views.ArtworkCreateView.as_view(), name='artwork_create'),
    path('artwork/<int:pk>/update/', views.ArtworkUpdateView.as_view(), name='artwork_update'),
    path('artwork/<int:pk>/delete/', views.ArtworkDeleteView.as_view(), name='artwork_delete'),
    ]