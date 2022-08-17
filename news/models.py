from django.db import models
from django.contrib.auth.models import User


# Create your models here.
article = 'AR'
news = 'MW'

POST_TYPE = [
    (article, 'Статья'),
    (news, 'Новость')
]


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)

    def update_rating(self):
        rank_update = 0
        for post in self.post_set.all():
            rank_update += 3 * post.rank
            for comment in post.comment_set.all():
                rank_update += comment.rank
        for comment in self.user.comment_set.all():
            rank_update += comment.rank
        self.rank = rank_update
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=2,
                            choices=POST_TYPE,
                            default=article)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    header = models.CharField(max_length=255)
    text = models.TextField()
    rank = models.IntegerField(default=0)

    def like(self):
        self.rank += 1
        self.save()

    def dislike(self):
        self.rank -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124]}...' if len(self.text) > 124 else self.text


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rank = models.IntegerField(default=0)

    def like(self):
        self.rank += 1
        self.save()

    def dislike(self):
        self.rank -= 1
        self.save()
