from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    COLLEGE_DEPARTMENTS = [
        ("CCS", "College of Computer Studies"),
        ("CNAHS", "College of Nursing & Allied Health Sciences"),
        ("CEA", "College of Engineering and Architecture"),
    ]

    YEAR_LEVELS = [
        ("1", "1st Year"),
        ("2", "2nd Year"),
        ("3", "3rd Year"),
        ("4", "4th Year"),
    ]

    college_dept = models.CharField(
        max_length=50, choices=COLLEGE_DEPARTMENTS, blank=True, null=True
    )
    course = models.CharField(max_length=100, blank=True, null=True)
    year_level = models.CharField(
        max_length=1, choices=YEAR_LEVELS, blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
