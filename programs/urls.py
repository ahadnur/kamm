from django.urls import path
from . import views

urlpatterns = [
    path('sanitation/', views.sanitation, name="sanitation"),
    path('health/', views.health, name="health"),
    path('awarness/', views.awarness, name="awarness"),
    path('handicraft/', views.handicraft, name="handicraft"),
    path('education/', views.education, name="education"),
]
