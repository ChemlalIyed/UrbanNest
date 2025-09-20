from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('products',views.ProductsView)
router.register('home',views.HomeView)
router.register('cart',views.Cart_View)
router.register('orders',views.OrdersView)
router.register('users',views.UserView)
router.register('phone',views.PhoneView)
urlpatterns = [
    path('',include(router.urls)),
    path('banne/',views.BanneUserView.as_view()),
    path('message_api/message=<str:text>',views.Message_api.as_view()),
    path("category/",views.CategorysView.as_view()),
    path("product/<int:id>/<str:token>/<int:i>",views.Like.as_view())
]