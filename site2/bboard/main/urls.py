from django.urls import path
from .views import index
from .views import other_page
from .views import BBLoginView
from .views import profile, profile_posts_add, profile_posts_delete
from .views import BBLogoutView
from .views import RegisterUserView, RegisterDoneView

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/login', BBLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/profile/add/', profile_posts_add, name='profile_posts_add'),
    path('accounts/profile/delete/<int:pk>', profile_posts_delete.as_view(), name='profile_posts_delete'),

]
