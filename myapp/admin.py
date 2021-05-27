from django.contrib import admin

from .models import PostMessage
from .models import Interaction
admin.site.register(Interaction)
admin.site.register(PostMessage)
# Register your models here.
