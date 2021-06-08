from django.contrib import admin
from .models import ReviewUser


@admin.register(ReviewUser)
class ReviewUserAdmin(admin.ModelAdmin):
    pass
