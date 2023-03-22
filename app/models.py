from django.db import models


class Payload(models.Model):
    content_html = models.TextField()
    subject = models.CharField(max_length=200)
    to_recipients = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class AttachFile(models.Model):
    payload = models.ForeignKey(
        Payload, on_delete=models.CASCADE, related_name="attach_files", null=True, blank=True)
    file_bytes = models.TextField()
    name = models.CharField(max_length=200)
    isInline = models.BooleanField(blank=True)
    content_id = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
