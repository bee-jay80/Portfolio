from django.db import models

# Create your models here.
    
class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(Tag,related_name="projects")
    link = models.URLField(max_length=200,blank=True)
    default_image = models.ImageField(upload_to="default_image/" ,default="Null")

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="images")
    image = models.ImageField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image"
    
class Skill(models.Model):
    name = models.CharField(max_length=100,unique=True)
    skill_image = models.ImageField(upload_to="skill_image/" ,default="Null")

    def __str__(self): 
        return self.name
