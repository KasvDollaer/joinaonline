from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Member, Product, Image, Sub_Category, Category, Reviews

# Define an inline admin descriptor for Member model
# which acts a bit like a singleton
class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'member'

class UserAdmin(BaseUserAdmin):
    inlines = (MemberInline, )

# Define inline image fields for the admin    
class ImageInline(admin.TabularInline):
    model = Image
    extra = 3

class ProductAdmin(admin.ModelAdmin):  
    # Add images to the add / edit product on the admin 
    inlines = [ImageInline]
    
    # You can view more options here: https://docs.djangoproject.com/en/1.10/intro/tutorial07/

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register Product and ProductAdmin
admin.site.register(Product, ProductAdmin)

#Category and SubCategory Models
admin.site.register(Category)
admin.site.register(Sub_Category)

#Review
admin.site.register(Reviews)
