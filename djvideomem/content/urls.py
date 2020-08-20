from django.urls import path
from .views import CourseListView, CourseDetailView

app_name = "content"

urlpatterns = [
    path("", CourseListView.as_view(), name='course-list'),
    path("<slug>/", CourseDetailView.as_view(), name='course-detail')
]