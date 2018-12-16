from django.contrib import admin
from .models import BlogIndexPage
from .models import BlogPage


admin.site.register(BlogIndexPage)
admin.site.register(BlogPage)

# Register your models here.
