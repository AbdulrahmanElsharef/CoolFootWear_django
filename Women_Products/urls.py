from django.contrib import admin
from django.urls import path

app_name='Women_Products'
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('products.urls',namespace='products')),
]
