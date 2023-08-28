from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=250)

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'


    def __str__(self):
        return '{}'.format(self.name)
class Courses(models.Model):
    name = models.CharField(max_length=250)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    class Meta:
        ordering=('name',)
        verbose_name='courses'
        verbose_name_plural='coursess'

    def __str__(self):
        return '{}'.format(self.name)