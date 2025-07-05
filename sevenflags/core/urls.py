from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),

    path("set-currency/", views.set_currency, name="set_currency"),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_details, name='blog_details'),
    path('contact/', views.contact, name='contact'),
    path('invest/', views.invest, name='invest'),
    path('properties/', views.properties, name='properties'),
    path('get_featured_properties/', views.get_featured_properties, name='get_featured_properties'),
    path('get_countries/', views.get_countries, name='get_countries'),
    path('get_cities/', views.get_cities, name='get_cities'),
    path('get_property_types/', views.get_property_types, name='get_property_types'),
    path('get_property_details/<int:id>/' ,views.get_property_details, name='get_property_details'),
    path("admin/update-rates/", views.update_exchange_rates_view, name="update_exchange_rates"),
]