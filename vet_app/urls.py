from django.urls import path
from .views import VetListView, VetDetailView, VetCreateView, VetUpdateView, SVListView
from . import views

urlpatterns = [
    path('', VetListView.as_view(), name='v_list'),
    path('<int:pk>/', VetDetailView.as_view(), name='v_detail'),
    path('new/', VetCreateView.as_view(), name='v_new'),
    path('<int:pk>/edit/', VetUpdateView.as_view(), name='v_edit'),
    path('svlist/', SVListView.as_view(), name='sv_list'),
    path('query1/', views.query1, name='query1'),
    path('query2/', views.query2, name='query2'),
]