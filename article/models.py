from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    published = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # if not self.slug:
        #    self.slug = slugify(self.name)
        super().save(*args, **kwargs)


def slugify_instance_title(instance, save=False):
    slug = slugify(instance.name)
    qs = Article.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        slug = f"{slug}-{qs.count()+1}"
    instance.slug = slug
    if save:
        instance.save()
    return instance


def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(article_pre_save, sender=Article)
