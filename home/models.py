from django.db import models
from django.utils.text import slugify
# Create your models here.


class Blog(models.Model):
    IS_ACTIVE = (
        ('T', 'Active'),
        ('F', 'In-Active'),
    )
    title = models.CharField(max_length=254)
    description = models.TextField()
    author = models.CharField(max_length=254)
    feature_image = models.ImageField(upload_to="blog/", height_field=None, width_field=None, max_length=None)
    is_active = models.CharField(max_length=1, choices=IS_ACTIVE)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title



