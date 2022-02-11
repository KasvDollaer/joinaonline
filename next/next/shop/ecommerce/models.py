from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mimage = models.ImageField(upload_to = 'members/' ,blank=True, null=True)
    phone_number = models.CharField(max_length=30)
    about = models.TextField()
    @property
    def photo_url(self):
         if self.mimage and hasattr(self.mimage, 'url'):
         
            return self.mimage.url

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    category_slug = models.SlugField(max_length=200, null=True, blank=True)
    category_image = models.ImageField(upload_to = 'category_banner/')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.category_slug = slugify(self.name)
        super(Category, self).save(*args,**kwargs)

class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sub_categories")
    subcategory_slug = models.SlugField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.subcategory_slug = slugify(self.name)
        super(Sub_Category, self).save(*args,**kwargs)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)
    sub_category = models.ForeignKey(Sub_Category, related_name='products', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    content = models.TextField()
    excerpt = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    author = models.PositiveIntegerField()
    featured_image = models.CharField(max_length=300)

    def __str__(self):
        return self.name
        
    
    
class Meta:
        db_table = 'members'

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/' ,blank=True, null=True)
