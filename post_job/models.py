from django.db import models

from users.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='image/',null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Tag(models.Model):
    SKILL_TAGS = [
    ('Python','Python'),
    ('JavaScript','JavaScript'),
    ('Django','Django'),
    ('React','React'),
    ('SQL','SQL'),
    ('Java','Java'),
    ('C#','C#'),
    ('AWS','AWS'),
    ('Docker','Docker'),
    ('Machine Learning','Machine Learning'),
    ('Data Analysis','Data Analysis'),
    ('UI/UX Design','UI/UX Design'),
    ('SEO','SEO'),
    ('Graphic Design','Graphic Design'),
    ]
    tag_name = models.CharField(max_length=255,unique=True,choices=SKILL_TAGS)

    def __str__(self):
        return self.tag_name

class Post(models.Model):

    JOB_TYPE_CHOICES = [
    ('Full Time employment', 'Full Time employment'),
    ('Part Time employment', 'Part Time employment'),
    ('Apprenticeship','Apprenticeship'),
    ('Internship', 'Internship'),
    ('Traineeship','Traineeship'),
    ('Contract employment', 'Contract employment'),
    ('Casual employment','Casual employment'),
    ('Seasonal employment','Seasonal employment'),
    ('Employment on commission','Employment on commission'),
    ('Leased employment','Leased employment'),
    ('Contingent employment','Contingent employment'),
    ('Probation','Probation'),
    ('Freelance','Freelance'),
    ('Temporary','Temporary'),
    ] 

    INDUSTRY_CHOICES = [
    ('Information Technology', 'Information Technology'),
    ('Healthcare', 'Healthcare'),
    ('Finance', 'Finance'),
    ('Education', 'Education'),
    ('Marketing', 'Marketing'),
    ('Engineering', 'Engineering'),
    ('Retail', 'Retail'),
    ('Customer Service', 'Customer Service'),
    ('Legal', 'Legal'),
    ]

    EXPERIENCE_CHOICES = [
        ('Fresher', 'Fresher'),
        ('Entry-level', 'Entry-level'),
        ('Mid-level', 'Mid-level'),
        ('Senior-level', 'Senior-level'),
        ('Manager', 'Manager'),
        ('Director', 'Director'),
    ]

    WORK_ENVIRONMENT_CHOICES = [
        ('Remote', 'Remote'),
        ('On-site', 'On-site'),
        ('Hybrid', 'Hybrid'),
    ]

    SALARY_RANGE_CHOICES = [
    ('Below 30K', 'Below 30K'),
    ('30K-50K', '30K-50K'),
    ('50K-80K', '50K-80K'),
    ('80K-100K', '80K-100K'),
    ('100K+', '100K+'),
    ]

    BENEFIT_TAGS = [
    ('Health Insurance','Health Insurance'),
    ('Paid Time Off','Paid Time Off'),
    ('Flexible Hours','Flexible Hours'),
    ('Remote Work','Remote Work'),
    ('Retirement Plan','Retirement Plan'),
    ('Stock Options','Stock Options'),
    ('Performance Bonus','Performance Bonus'),
    ('Gym Membership','Gym Membership'),
    ('Relocation Support','Relocation Support'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=200,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    job_type = models.CharField(max_length=100, choices=JOB_TYPE_CHOICES,default='None')
    location = models.CharField(max_length=200,default='Not Specified')
    skill_tag = models.ManyToManyField(Tag, blank=True) 
    # salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary = models.CharField(choices=SALARY_RANGE_CHOICES, null=True, blank=True)
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES,null=True, blank=True)
    experience_level = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES,default='Fresher')
    work_environment = models.CharField(max_length=20, choices=WORK_ENVIRONMENT_CHOICES,blank=True,null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
    
    
    
    
    
    