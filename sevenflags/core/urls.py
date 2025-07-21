from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),

    path("set-currency/", views.set_currency, name="set_currency"),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
<<<<<<< HEAD
    path('blog/<slug:slug>/', views.blog_details, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('invest/', views.invest, name='invest'),
    path('properties/', views.properties, name='properties'),
    path('property/<int:id>/', views.get_property_details, name='property_detail'),
=======
    path('blog/<int:id>/', views.blog_details, name='blog_details'),
    path('contact/', views.contact, name='contact'),
    path('invest/', views.invest, name='invest'),
    path('properties/', views.properties, name='properties'),
>>>>>>> abd6e6963a5a6f7286b33ee5e28834dc413f58f0
    path('get_featured_properties/', views.get_featured_properties, name='get_featured_properties'),
    path('get_countries/', views.get_countries, name='get_countries'),
    path('get_cities/', views.get_cities, name='get_cities'),
    path('get_property_types/', views.get_property_types, name='get_property_types'),
    path('get_property_details/<int:id>/' ,views.get_property_details, name='get_property_details'),
<<<<<<< HEAD
    path('contact/', views.contact, name='contact'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
    # path('send-newsletter/', views.send_newsletter, name='send_newsletter'),
=======
>>>>>>> abd6e6963a5a6f7286b33ee5e28834dc413f58f0
    path("admin/update-rates/", views.update_exchange_rates_view, name="update_exchange_rates"),
]