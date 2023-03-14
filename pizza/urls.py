from django.urls import path
from pizza import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home),
    path('signup',views.register,name='signup'),
    path('login',views.signin,name='login'),
    path('/account/login/',views.signin,name='/login'),
    path('home',views.home,name='home'),
    path('home/<slug:data>',views.home,name='home'),
    path('signout',views.signout,name='signout'),
    path('cart',views.cart,name='cart'),
    path('footer',views.createView.as_view(),name='footer'),
    path('generic',views.genericview.as_view()),
    path('success',views.success,name='success'),
    path('orderapi',views.order_api,name='orderapi'),
    path('orders_list',views.orders_list,name='orders_list'),
    path('<slug:data>',views.home,name='filter'),
    path('addtocart/<slug:uid>',views.add_to_cart,name='addtocart'),
    path('deleteitem/<slug:uid>',views.delete_item,name='deleteitem'),
    
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)