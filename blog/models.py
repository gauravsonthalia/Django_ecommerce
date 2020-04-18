from django.db import models

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    head0 = models.CharField(max_length=500, default=True)
    chead0 = models.CharField(max_length=5000, default=True)
    head1 = models.CharField(max_length=500, default=True)
    chead1 = models.CharField(max_length=5000, default=True)
    head2 = models.CharField(max_length=500, default=True)
    chead2 = models.CharField(max_length=5000, default=True)
    pub_date = models.DateField()  
    image = models.ImageField(upload_to='blog/images', default = '')


    def __str__(self):
        return self.title
    