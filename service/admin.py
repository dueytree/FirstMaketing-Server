from django.contrib import admin
from .models import Recruit, Comment


@admin.register(Recruit)
class RecruitAdmin(admin.ModelAdmin):
    # list_display = ["photo", "product"]
    # list_display_links = ["product"]
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
