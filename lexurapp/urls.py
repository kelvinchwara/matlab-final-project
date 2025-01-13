
from django.contrib import admin
from django.urls import path

from lexurapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('events', views.events, name='events'),
    path('chef/', views.chef, name='chef'),
    path('gallery/', views.gallery, name='gallery'),
    path('menu/', views.menu, name='menu'),
    path('rooms/', views.rooms, name='rooms'),
    path('contact/', views.contact, name='contact'),
    path('showcontact/', views.showcontact, name='showcontact'),
    path('book/', views.book, name='book'),
    path('bookingdetails/', views.bookingdetails, name='bookingdetails'),
    path('order/', views.order, name='order'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('updategallery/', views.update_gallery, name='updategallery'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('editcontact/<int:id>/', views.editcontact, name='editcontact'),
    path('editorders/<int:id>/', views.editorders, name='editorders'),
    path('showorder/', views.showorder, name='showorder'),
    path('update/<int:id>/', views.update, name='update'),
    path('updatecontact/<int:id>/', views.updatecontact, name='updatecontact'),
    path('updateorders/<int:id>/', views.updateorders, name='updateorders'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('delete_contact/<int:id>/', views.delete_contact, name='delete_contact'),
    path('delete_room/<int:id>/', views.delete_room, name='delete_room'),
    path('delete_order/<int:id>/', views.delete_order, name='delete_order'),






]
