from django.urls import path
from . import views

urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products),
    path('save-saving-products/', views.save_saving_products),
    path('deposit-products/', views.deposit_products),    
    path('saving-products/', views.saving_products),
    path('deposit-product-detail/<str:fin_prdt_cd>/', views.deposit_product_detail),    
    path('saving-product-detail/<str:fin_prdt_cd>/', views.saving_product_detail),   
]
