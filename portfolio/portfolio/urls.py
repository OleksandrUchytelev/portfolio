from django.contrib import admin
from django.urls import path
from portfolioApp import views
from django.views.generic import RedirectView


handler404 = 'portfolioApp.views.handle_404'
handler500 = 'portfolioApp.views.handle_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='articles/')),
    path('articles/', views.articles_view, name='articles'),
    path('skills/', views.skills_view, name='skills'),
    path('projects/', views.projects_view, name='projects'),
    path('career/', views.career_view, name='career'),
]
