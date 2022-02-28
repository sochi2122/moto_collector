from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('motorcycles/', views.motorcycles_index, name='index'),
    path('motorcycles/<int:motorcycle_id>/', views.motorcycles_detail, name='detail'),
    path('motorcycles/create/', views.MotorcycleCreate.as_view(), name='motorcycles_create'),
    path('motorcycles/<int:pk>/update/', views.MotorcycleUpdate.as_view(), name='motorcycles_update'),
    path('motorcycles/<int:pk>/delete/', views.MotorcycleDelete.as_view(), name='motorcycles_delete'),

    path('motorcycles/<int:motorcycle_id>/add_mile/', views.add_mile, name='add_mile'),


    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),

    
    path('motorcycles/<int:motorcycle_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),   
    path('motorcycles/<int:motorcycle_id>/add_photo/', views.add_photo, name='add_photo'),

]