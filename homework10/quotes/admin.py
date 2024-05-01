from django.contrib import admin
from .models import Tag, Quotes, Author

# Register your models here.
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Quotes)