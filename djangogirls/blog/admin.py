from django.contrib import admin
from .models import Post

#to make our model visible on admin page
admin.site.register(Post)