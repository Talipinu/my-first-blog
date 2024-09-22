from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)       # Lasse die Admin-App Posts verwalten
admin.site.register(Comment)    # Lasse die Admin-App Kommentare verwalten