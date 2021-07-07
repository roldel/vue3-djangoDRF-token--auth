from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.responsetest),
]


from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]