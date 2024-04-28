from django.urls import path
from . import views

urlpatterns = [
    path("", views.board_list),
    path("<int:pk>/", views.board_detail),
]
