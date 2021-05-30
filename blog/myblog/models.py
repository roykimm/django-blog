from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    head_image = models.ImageField(
        upload_to='myblog/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author : 추후 작성예정

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/myblog/{self.pk}/'
