
from django.urls import path
from app import views


urlpatterns = [
    path('index/',views.Student.as_view({'post':'post'}))
]
