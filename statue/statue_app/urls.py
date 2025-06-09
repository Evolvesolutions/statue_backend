from django.urls import path
from . import views



urlpatterns=[

    path('api/',views.statue_list, name='statue-list'),
    # path('api/<int:pk>/', views.statue_detail, name='statue-detail'),
    # path('Home_list/', views.Home_list),

]
