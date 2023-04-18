from django.db import models


class Tweet(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=50)
    created_at = models.DateField(max_length=50)
    autor = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=20)
    date = models.DateField()
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Mark(models.Model):
    mark_value = models.CharField(max_length=30)
    tweet = models.CharField(max_length=50)

    def __str__(self):
        return self.mark_value

