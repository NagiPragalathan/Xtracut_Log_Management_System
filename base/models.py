from django.db import models
import uuid

class LogModel(models.Model):
    userid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    log_msg = models.TextField()
    StatusCode = models.CharField(max_length=255)
    user_mailid = models.EmailField()
    Plugin = models.CharField(max_length=255)
    function = models.CharField(max_length=255)
    dateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.log_msg
    