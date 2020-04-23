from django.contrib import admin
from .models import ContactFormModel, HomeImage,Depart1, Depart2, Depart3, Depart4, Opinion, Youtube
from django.db import models
from tinymce.widgets import TinyMCE


@admin.register(ContactFormModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]
    list_filter = ('الاسم', 'الرقم', "timestamp")

    pass

class VideoAdmin(admin.ModelAdmin):
    # fields = ["tutorial_title",
    #           "tutorial_published",
    #           "tutorial_content"]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
    
admin.site.register(Youtube, VideoAdmin)    

admin.site.register(HomeImage)

admin.site.register(Depart1)

admin.site.register(Depart2)

admin.site.register(Depart3)

admin.site.register(Depart4)

admin.site.register(Opinion)

# admin.site.register(Item)
