from django.contrib import admin
from .models import Topic, Recipe, Ingredient

def duplicate_jorn(modeladmin, request, queryset):
    post_url = request.META['HTTP_REFERER']

    for object in queryset:
        object.id = None
        object.name = object.name+'-b'
        object.save()

    return HttpResponseRedirect(post_url)
 
admin.site.register(Recipe)
admin.site.register(Topic)
admin.site.register(Ingredient)
