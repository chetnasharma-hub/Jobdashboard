from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer



@api_view(["POST"])
def duplicate_job(request, pk):
    try:
        job = Job.objects.get(pk=pk)

        new_job = Job.objects.create(
            title=f"{job.title} (Copy)",
            status=job.status,          
            category=job.category,
            address=job.address,
            city=job.city,
            state=job.state,
            start_date=job.start_date,
            end_date=job.end_date,
            description=job.description,
            job_profile_pic=job.job_profile_pic 
        )

        return Response(
            {
                "message": "Job duplicated successfully",
                "id": new_job.id
            },
            status=status.HTTP_201_CREATED
        )

    except Job.DoesNotExist:
        return Response(
            {"error": "Job not found"},
            status=status.HTTP_404_NOT_FOUND
        )



from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import Job

class JobStatusStatsAPIView(APIView):
    def get(self, request):
        data = (
            Job.objects
            .values('status')
            .annotate(count=Count('id'))
        )

        total = Job.objects.count()

        result = []
        for item in data:
            percentage = (item['count'] / total) * 100 if total > 0 else 0
            result.append({
                "status": item['status'],
                "count": item['count'],
                "percentage": round(percentage, 2)
            })

        return Response(result)
