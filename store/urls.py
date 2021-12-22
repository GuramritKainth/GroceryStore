from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.customer_list),
    path('customer/<int:id>/', views.customer_detail),
    path('groceryitem/', views.GroceryItemList.as_view()),
    path('groceryitem/<int:id>/', views.GroceryItemDetail.as_view()),
    # path('groceryitem/', views.list_grocery_item),
    path('purchase/', views.PurchaseList.as_view()),
    path('purchase/<int:id>/', views.PurchaseDetail.as_view()),
    # path('purchase/', views.list_purchase),
]
