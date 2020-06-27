from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField('Status', default=True)
    created = models.DateField('Created', auto_now=False, auto_now_add=True)
    updated = models.DateField('Updated', auto_now=True, auto_now_add=False)
    deleted = models.DateField('Deleted', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Category(ModelBase):
    name = models.CharField('Name', max_length=100, unique=True)
    image = models.ImageField('Image', upload_to='category/')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str(self):
        return self.name


class Author(ModelBase):
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=120)
    email = models.EmailField('Email', max_length=200)
    description = models.TextField('Description')
    author_url = models.URLField('Author Url', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return '{0},{1}'.format(self.first_name, self.last_name)


class Post(ModelBase):
    title = models.CharField('Title', max_length=150, unique=True)
    slug = models.CharField('Slug', max_length=150, unique=True)
    description = models.TextField('Description')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = RichTextField()
    image = models.ImageField('Image', upload_to='img/', max_length=255)
    published = models.BooleanField('Published', default=False)
    date_published = models.DateField('Date Published')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class Company(ModelBase):
    about_us = models.TextField('About Us')
    phone = models.CharField('Phone', max_length=10)
    email = models.EmailField('Email', max_length=200)
    address = models.CharField('Address', max_length=200)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.about_us


class SocialNetwork(ModelBase):
    facebook = models.URLField('Facebook', max_length=200, null=True, blank=True)
    twitter = models.URLField('Twitter', max_length=200, null=True, blank=True)
    instagram = models.URLField('Instagram', max_length=200, null=True, blank=True)
    tik_tok = models.URLField('Tik Tok', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Social Network'
        verbose_name_plural = 'Social Networks'

    def __str(self):
        return self.facebook


class Contact(ModelBase):
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=150)
    email = models.EmailField('Email', max_length=200)
    subject = models.CharField('Subject', max_length=100)
    message = models.TextField('Message')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.subject


class Subscriber(ModelBase):
    email = models.EmailField('Email', max_length=200)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email

