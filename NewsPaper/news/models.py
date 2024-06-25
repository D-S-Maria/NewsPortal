from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        sum_rating_ar = 0
        sum_rating_com = 0
        sum_rating_ar_com = 0

        posts = Post.objects.filter(author_post=self)
        for i in posts:
            sum_rating_ar += i.rating
        comments = Comment.objects.filter(user=self.user)
        for i in comments:
            sum_rating_com += i.rating

        posts_comments = Comment.objects.filter(post__author_post=self)
        for i in posts_comments:
            sum_rating_ar_com += i.rating

        self.rating = sum_rating_ar * 3 + sum_rating_com + sum_rating_ar_com
        self.save()



class Category(models.Model):
    name_category = models.CharField(max_length=50, unique=True)


class Post(models.Model):
    article = 'AR'
    news = 'NE'
    TYPES = [(article, 'статья'), (news, 'новость')]
    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPES, default=article)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
