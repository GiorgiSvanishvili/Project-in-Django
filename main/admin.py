from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from django.db import models 

admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial)