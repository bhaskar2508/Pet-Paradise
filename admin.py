from django.contrib import admin

# Register your models here.

from.models import Catgory,CatFood,CatFoodCart,CatHealth,CatHealthCart,CatToys,CatToysCart,DogFood,DogFoodCart,DogHealth,DogHealthCart,DogToys,DogToysCart

class CategryAdmin(admin.ModelAdmin):
    list_display=['name','description']
    list_filter=['name']
admin.site.register(Catgory,CategryAdmin)


class CatFoodAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'description', 'image', 'category']
    list_filter = ['category', 'product_price']  
admin.site.register(CatFood,CatFoodAdmin)

class CatFoodCartAdmin(admin.ModelAdmin):
    list_display=['user','catfood']
    list_filter=['user']
admin.site.register(CatFoodCart,CatFoodCartAdmin)

class CatHealthAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'description', 'image', 'category']
    list_filter = ['category', 'product_price']  
admin.site.register(CatHealth,CatHealthAdmin)

class CatHealthCartAdmin(admin.ModelAdmin):
    list_display=['user','cathealth']
    list_filter=['user']
admin.site.register(CatHealthCart,CatHealthCartAdmin)

class CatToysAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'description', 'image', 'category']
    list_filter = ['category', 'product_price']  
admin.site.register(CatToys,CatToysAdmin)

class CatToysCartAdmin(admin.ModelAdmin):
    list_display=['user','cattoys']
    list_filter=['user']
admin.site.register(CatToysCart,CatToysCartAdmin)

class DogFoodAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'description', 'image', 'category']
    list_filter = ['category', 'product_price']  
admin.site.register(DogFood,DogFoodAdmin)

class DogFoodCartAdmin(admin.ModelAdmin):
    list_display=['user','dogfood']
    list_filter=['user']
admin.site.register(DogFoodCart,DogFoodCartAdmin)

class DogToysAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'description', 'image', 'category']
    list_filter = ['category', 'product_price']  
admin.site.register(DogToys,DogToysAdmin)

class DogToysCartAdmin(admin.ModelAdmin):
    list_display=['user','dogtoys']
    list_filter=['user']
admin.site.register(DogToysCart,DogToysCartAdmin)

class DogHealthAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'description', 'image', 'category']
    list_filter = ['category', 'product_price']  
admin.site.register(DogHealth,DogHealthAdmin)

class DogHealthCartAdmin(admin.ModelAdmin):
    list_display=['user','doghealth']
    list_filter=['user']
admin.site.register(DogHealthCart,DogHealthCartAdmin)
