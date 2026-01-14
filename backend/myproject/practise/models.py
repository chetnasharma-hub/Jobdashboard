from django.db import models

    
class Job(models.Model):
    job_profile_pic=models.ImageField(upload_to="job_pic/",null=True,blank=True)
    title = models.CharField(max_length=200)
    STATUS = [
        ('Draft', 'Draft'),
        ('Requested', 'Requested'),
        ('Posted', 'Posted'),
        ('Filled', 'Filled'),
    ]
    status = models.CharField( max_length=20, choices=STATUS, default='draft')        
    
    CATEGORIES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('Internship', 'Internship'),
        ('volunteer', 'Volunteer'),
    ]

    category = models.CharField( max_length=20, choices=CATEGORIES, default='full_time')
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    start_date=models.DateField(blank=True,null=True)
    end_date=models.DateField(blank=True,null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return self.title
    