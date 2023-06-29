from django.contrib import admin

# Register your models here.
from .models import Question,Choice,next,conclusion

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(next)
admin.site.register(conclusion)