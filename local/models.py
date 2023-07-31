from django.db import models

# Create your models here.C
# class Course(models.Model):
#     Coursename=models.CharField(max_length=30)
#     Code=models.IntegerField()
#     Collage=models.CharField(max_length=28)
#     Student=models.CharField(max_length=20)


#     def __str__(self):
#         return self.Coursename



class Course_detail(models.Model):
    Coursename=models.CharField(max_length=30)
    Code=models.IntegerField()
    Collage=models.CharField(max_length=28)
    Student=models.CharField(max_length=20)


    def __str__(self):
        return self.Coursename
    

    


    
