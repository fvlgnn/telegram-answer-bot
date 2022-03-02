from django.db import models


class Chat(models.Model):

    chat_id = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    tipology = models.CharField(max_length=32, default='private')
    enable = models.BooleanField(default=False)
    details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.chat_id)


class Answer(models.Model):
    
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("message",)

    def __str__(self):
        return self.message


class Keyword(models.Model):

    keyword = models.CharField(max_length=32)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="answer")
    enable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("keyword",)

    def __str__(self):
        return self.keyword


class Broadcast(models.Model):
    
    title = models.CharField(max_length=64)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title
