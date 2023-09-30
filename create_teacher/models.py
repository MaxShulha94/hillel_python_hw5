from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return (
            f"Name: {self.first_name}, Surname: {self.last_name}, Date of birth: {self.birth_date}, "
            f"Subject: {self.subject}; "
        )
