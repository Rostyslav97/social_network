from django.db import models
from django.conf import settings
from shared.models import TimeStampMixin


class Post(TimeStampMixin):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=False, on_delete=models.SET_NULL)


    def __str__(self) -> str:
        return f"{self.title}"

    
    # def get_absolute_url(self):
    #     return reverse('post', args=[str(self.id)])


class Like(TimeStampMixin):
    post = models.ForeignKey("Post", null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True)