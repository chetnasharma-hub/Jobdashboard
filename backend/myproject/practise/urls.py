from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet,duplicate_job, JobStatusStatsAPIView

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')  

urlpatterns = [
    path('api/', include(router.urls)), 
     path("jobs/<int:pk>/duplicate/", duplicate_job),
    path('job-status-stats/', JobStatusStatsAPIView.as_view()),

    
]
