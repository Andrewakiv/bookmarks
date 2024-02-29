from django.conf import settings
from django.db import models, IntegrityError
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)
    total_likes = models.PositiveIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['-total_likes'])
        ]
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('bookmarks:detail', args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            try:
                self.slug = slugify(self.title)
                super().save(*args, **kwargs)
            except IntegrityError:
                self.slug = f"{self.slug}-{timezone.now().strftime('%f')}"
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title

