"""
URL configuration for online_prestige_watch_marketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('',views.public_home),
    path('log',views.Login),
    path('signup',views.signup),
    path('adminhome',views.adminhome),
    path('Customer',views.Customer),
    path('Staff',views.Staff),
    path('adminupdatestaff/<id>',views.adminupdatestaff),
    path('admin_inactive_staff/<id>',views.admin_inactive_staff),
    path('admin_active_staff/<id>',views.admin_active_staff),
    path('Category',views.Category),
    path('adminupdatecategory/<id>',views.adminupdatecategory),
    path('Subcategory',views.Subcategory),
    path('adminupdatesubcategory/<id>',views.adminupdatesubcategory),
    path('Brand',views.Brand),
    path('adminupdatebrand/<id>',views.adminupdatebrand),
    path('view_item',views.view_item),
    path('adminupdateitem/<id>',views.adminupdateitem),
    path('Sales',views.adminsales),
    path('adminreview',views.adminreview),
    path('admin_assign_verification',views.admin_assign_verification),
    path('verify_item/<id>',views.verify_item),
    path('admin_delivery_status',views.admin_delivery_status),
    # path('update_order_status',views.update_order_status),
    # path('adminassignfield',views.adminassignfield),
    
    path('wstaff_home',views.wstaff_home),
    path('Staff_customer',views.Staff_customer),
    path('Staff_Category',views.Staff_Category),
    path('staffupdatecategory/<id>',views.staffupdatecategory),
    path('Staff_Subcategory',views.Staff_Subcategory),
    path('staffupdatesubcategory/<id>',views.staffupdatesubcategory),
    path('Staff_Brand',views.Staff_Brand),
    path('staffupdatebrand/<id>',views.staffupdatebrand),
    path('Staff_item',views.Staff_item),
    path('Assign_field',views.Assign_field),
    path('Staff_sales',views.Staff_sales),
    path('Staff_review',views.Staff_review),
    
    
    path('customer_home',views.customer_home),
    path('customer_profile',views.customer_profile),
    path('customer_review',views.customer_review),
    path('cust_add_item_review/<id>',views.cust_add_item_review),
    path('customer_cart',views.customer_cart),
    # path('cust_view_products',views.cust_view_products),
    path('customer_aboutus',views.customer_aboutus),
    path('index',views.temp),
    path('admin_index',views.tempy),
    path('cust_view_products',views.cust_view_products),
    path('addtocart/<id>',views.addtocart),
    path('increase_qty/<id>',views.increase_qty),
    path('decrease_qty/<id>',views.decrease_qty),
    path('delete_cart/<id>',views.delete_cart),
    path('customer_order/<id>',views.customer_order),
    path('customer_payment/<id>',views.customer_payment),
    path('cust_view_bill/<id>',views.cust_view_bill),
    path('cust_view_paid_orders',views.cust_view_paid_orders),
    path('cust_view_single_product_bill/<id>',views.cust_view_single_product_bill),
    path('cust_view_orderd_items/<id>',views.cust_view_orderd_items),
    path('cust_sell_itemss',views.cust_sell_itemss),
    path('cust_sell_itemss_update/<id>',views.cust_sell_itemss_update),
    path('Sell_now_button/<id>',views.Sell_now_button),
    path('selling_product_status',views.selling_product_status),
    path('cust_view_bill_for_sold_product/<itemid>',views.cust_view_bill_for_sold_product),
    path('disclaimer',views.disclaimer),
    path('adminorderview',views.adminorderview),
    path('admin_assign_order/<id>',views.admin_assign_order),
    path('product_add/<id>',views.product_add),

    path('fstaff_home',views.fstaff_home),  
    path('fwork_view_order',views.fwork_view_order),
    path('fstaff_update_staff/<id>',views.fstaff_update_staff),
    path('fwork_view_verifyy',views.fwork_view_verifyy),
    path('fstaff_verify_update_status/<id>',views.fstaff_verify_update_status),
    
    
]
