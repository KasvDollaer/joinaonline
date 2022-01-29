from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30)
    about = models.TextField()
    is_customer = models.BooleanField(null=True)


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
    picture = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
	# Private Information
	first_name = models.CharField(max_length=50, default='')
	last_name = models.CharField(max_length=50, default='')
	email = models.EmailField()
	phone = models.CharField(max_length=15, default='')

	# Geographical Information
	address = models.CharField(max_length=150, default='')
	city = models.CharField(max_length=50, default='')
	company = models.CharField(max_length=100, null=True, blank=True, default='')
	zip_code = models.CharField(max_length=10, default='')
	state = models.CharField(max_length=50, null=True, blank=True, default='')
	country = models.CharField(max_length=50, null=True, blank=True, default='Zimbabwe')
	order_notes = models.CharField(max_length=10000, null=True, blank=True )

	# Delivery Method
	# delivery_choices = (
	# 	('pickup', 'Pickup'),
	# 	('express', 'Oloja Express')
	# 	)

	# delivery_method = models.CharField(max_length=13, choices=delivery_choices, default='express')

	# Payment Method
	payment_choices = (
		('Paynow', 'Paynow'),
		
		)

	payment_method = models.CharField(max_length=20, choices=payment_choices, default='Paynow')

	# Date and Time Information
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	paid = models.BooleanField(default=False) # Payment status

	def __str__(self):
		return 'Order %s' % self.id

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())



class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return 'order item %s' % self.id

	def get_cost(self):
		return self.price * self.quantity


    

    
    


# class Image(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='products/' ,blank=True, null=True)



#NEW MODELS DESIGN 


# class Products(models.Model):
#     name = models.CharField(max_length=1000)
#     price = models.FloatField()

#     pass
#     def __str__(self):
#         return self.name

# class OrderItem(models.Model):
#     pass
#     def __str__(self):
#         return self.name
# class Order(models.Model):
#     user = models.ForeignKey(Member, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Products)
#     start_date = models.DateTimeField(auto_now=True)
#     ordered = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.user.username
