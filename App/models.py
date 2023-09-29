from django.db import models

# Create your models here.

class Skill(models.Model):
  lang = models.CharField(max_length= 100)
  description = models.TextField()
  def __str__(self):
    return (self.lang)

class Portfolio(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_source_link = models.URLField()
    project_link_code = models.URLField()
    project_type = models.CharField(max_length=100)
    img = models.ImageField(upload_to='portfolio_images/')
    def __str__(self):
        return (self.project_name)

class About (models.Model):
   name = models.CharField(max_length=100)
   about_me = models.TextField()
   def __str__(self):
      return (self.name)
