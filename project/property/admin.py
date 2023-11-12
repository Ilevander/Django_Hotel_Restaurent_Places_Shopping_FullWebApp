from django.contrib import admin
from .models import Property, PropertyImages, PropertyReview, Category, PropertyBook, Place
#Transform TextField into an editor like World : 
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name','price','get_avg_rating','check_avalblity']

admin.site.register(Property,SomeModelAdmin)



class PropertyBookAdmin(admin.ModelAdmin):
    list_display = ['property','in_progress']

admin.site.register(PropertyBook,PropertyBookAdmin)



admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Category)
admin.site.register(Place)





