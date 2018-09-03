from django.urls import path

from . import views

app_name = 'polls4'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('owner', views.owner, name='owner'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

