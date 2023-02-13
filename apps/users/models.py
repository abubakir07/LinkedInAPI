from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.PhoneValidates import phone_regex


class User(AbstractUser):
    username = models.CharField(
        verbose_name='username',
        max_length=12,
        unique=True
    )
    image = models.ImageField(
        upload_to='user_images/',
        verbose_name='image',
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        verbose_name='phone_number',
        validators=[phone_regex],
        max_length=17,
        unique=True,
    )
    bio = models.TextField(
        verbose_name='bio',
        null=True,
        blank=True
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='create_at'
    )
    
    class Meta:
        verbose_name = "user"
        verbose_name_plural = 'Users'

    def __str__(self):
       return f'Username: {self.username}'


class Education(models.Model):
    title = models.CharField(
        verbose_name='education name',
        max_length=100)
    description = models.TextField(
        verbose_name='description',
        null=True,
        blank=True
    )
    faculty = models.CharField(
        verbose_name='faculty',
        max_length=100,
        null=True,
        blank=True
        )
    start_date = models.DateField(
        auto_now=True,
        verbose_name='start date'
    )
    end_date = models.DateField(
        auto_now=True,
        verbose_name='end date',
        null=True,
        blank=True
    )
    graduated = models.BooleanField(
        verbose_name='graduated',
        default=False
        )
    owner = models.ForeignKey(
    User, 
    on_delete=models.DO_NOTHING,
    related_name='user_educattion',
    verbose_name='user_educattion',
    null=True,
    blank=True
)

    class Meta:
        verbose_name = "education"
        verbose_name_plural = 'Educations'

    def __str__(self):
        return f'{self.title}---{self.faculty}'
    

class Skills(models.Model):
    name = models.CharField(
        verbose_name='skill name',
        max_length=100,
        unique=True
        )
    class Meta:
        verbose_name = "skill"
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f' ● {self.name}'


class WorkExperience(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Freelance', 'Freelance'),
        ('Internship', 'Internship'),
        ('Other', 'Other'),
    ]
    WORKPLACE_TYPE_CHOICES = [
        ('Office', 'Office'),
        ('Remote', 'Remote'),
        ('Other', 'Other'),
    ]

    job_title = models.CharField(
        verbose_name='job_title',
        max_length=100,
        null=True,
        blank=True
        )
    job_type = models.CharField(
        verbose_name='job_type',
        max_length=20,
        choices=JOB_TYPE_CHOICES,
        )
    company_name = models.CharField(
        verbose_name='company_name',
        max_length=100,
        null=True,
        blank=True
        )
    position = models.CharField(
        verbose_name='position',
        max_length=100,
        null=True,
        blank=True)
    location = models.CharField(
        verbose_name='location',
        max_length=100,
        null=True,
        blank=True
        )
    workplace_type = models.CharField(
        choices=WORKPLACE_TYPE_CHOICES,
        verbose_name='workplace_type',
        max_length=20,
        null=True,
        blank=True
        )
    currently_working = models.BooleanField(
        verbose_name='currently_working',
        default=False
        )
    start_date = models.DateField(
        auto_now=True,
        verbose_name='start_date'
    )
    end_date = models.DateField(
        verbose_name='end_date',
        auto_now=True,
        null=True,
        blank=True
        )
    description = models.TextField(
        verbose_name='',
        max_length=2000,
        null=True,
        blank=True
        )
    skills = models.ManyToManyField(
        Skills,
        related_name='skills',
        verbose_name='skills',
        null=True,
        blank=True
        )
    owner = models.ForeignKey(
        User, 
        on_delete=models.DO_NOTHING,
        related_name='user_work_exp',
        verbose_name='user_work_exp',
    )

    class Meta:
        verbose_name = "work experience"
        verbose_name_plural = 'Work Experiences'

    def __str__(self):
        return f'Company: {self.company_name}---{self.position}'
    