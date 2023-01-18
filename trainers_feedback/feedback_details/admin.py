from django.contrib import admin
from feedback_details.models import trainer_data
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(trainer_data)
# admin.site.register(trainer_feedback)