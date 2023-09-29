from django.contrib import admin

from . models import Skill
from . models import Portfolio, About

# Register your models here.
admin.site.register (Skill)
admin.site.register (Portfolio)
admin.site.register (About)