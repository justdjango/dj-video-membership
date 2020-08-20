from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Course, Video

class CourseListView(generic.ListView):
    template_name = "content/course_list.html"
    queryset = Course.objects.all()


class CourseDetailView(generic.DetailView):
    template_name = "content/course_detail.html"
    queryset = Course.objects.all()


class VideoDetailView(generic.DetailView):
    template_name = "content/video_detail.html"

    def get_object(self):
        video = get_object_or_404(Video, slug=self.kwargs["video_slug"])
        return video

    def get_queryset(self):
        course = get_object_or_404(Course, slug=self.kwargs["slug"])
        return course.videos.all()