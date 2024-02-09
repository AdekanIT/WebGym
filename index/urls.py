from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('branches/<int:pk>', views.get_all_branch),
    path('instructor/<int:pk>', views.get_full_inst),
    path('search', views.search_in, name='search'),
    path('order-list', views.get_all_orders),
    path('accounts/logout/', views.logout_review),
    path('sign-up', views.sign_up),
]