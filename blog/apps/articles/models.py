import datetime

from django.db import models

from django.utils import timezone
# Create your models here.
class Article(models.Model):
    articleTitle=models.CharField('Article name',max_length=200)
    articleText=models.TextField('Article text',max_length=10000)
    publicationDate=models.DateTimeField('Publication date')
    def __str__(self):
        return self.articleTitle

    def wasPublishedRecently(self):
        return self.publicationDate>=(timezone.now()-datetime.timedelta(days=7))

class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    authorName=models.CharField('Author name',max_length=50)
    content=models.CharField('comment content',max_length=500)
    pubDate=models.DateTimeField('Pub date')
    def __str__(self):
        return self.authorName

class Message(models.Model):
    nick=models.CharField('Nick',max_length=50)
    message=models.CharField('Message',max_length=500)
