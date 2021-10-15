from django.contrib import admin

from .models import Opros, Question, Variant, Finishedpoll, Answer

# Register your models here.
admin.site.register(Opros)
admin.site.register(Question)
admin.site.register(Variant)
admin.site.register(Finishedpoll)
admin.site.register(Answer)
