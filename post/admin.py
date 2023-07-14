from django.contrib import admin
from .models import CounselComment, CounselPost, CounselRecomment, JarPost
# Register your models here.
admin.site.register(CounselComment)
admin.site.register(CounselPost)
admin.site.register(CounselRecomment)
admin.site.register(JarPost)