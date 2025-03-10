from django.db import models


class BaseModel(models.Model):
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Region(BaseModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Department(BaseModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(BaseModel):
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=20,blank=True, null=True)
    email = models.CharField(max_length=75)
    data_file = models.FileField(upload_to='uploads/')
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
