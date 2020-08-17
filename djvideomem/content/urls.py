from django.urls import path
from .views import CourseListView

app_name = "content"

urlpatterns = [
    path("", CourseListView.as_view(), name='course-list')
]