from django.db import models


class ClubMember(models.Model):

    ROLE_CHOISES = (
        ('P', 'Palyer'),
        ("C", 'Coach')
    )
    name = models.CharField(max_length=50, null=False, blank=False)
    age = models.PositiveSmallIntegerField(blank=False, null=False)
    expr_years_in_sk = models.PositiveSmallIntegerField(blank=False, null=False)
    image = models.ImageField(upload_to="members/")
    joined_at = models.DateField()
    role = models.CharField(max_length=10, choices=ROLE_CHOISES, default="P")


    def __str__(self):
        return f'{self.name} joined us at {self.joined_at}'


class News(models.Model):

    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=2000, null=False, blank=False)
    image = models.ImageField(upload_to="news/")
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'id: {self.id}, title:{self.title}, description:{self.description}, published_at:{self.published_at}'



class Banner(models.Model):

    image = models.ImageField(upload_to='banner/')

