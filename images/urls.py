from django.urls import path
from . import views
urlpatterns = [
    path('media/<str:img>/',views.image)
]
