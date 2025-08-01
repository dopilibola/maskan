from django.urls import path, include
from .import views



urlpatterns = [
    path('', views.home, name='home' ),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout' ),
    path('register/', views.register_user, name='register'),
    path('update_password/', views.update_password, name='update_password' ),
    path('/one-to-one/', include('one_to_one.urls')),
    path('profile/', views.edit_profile, name='profile'),
    path('profiledet/', views.profile_detail, name='profile_detail'),

    # path('api/cemeteries/', views.get_cemeteries, name='get-cemeteries'),
    # path('api/cemeteries/<int:cemetery_id>/graves/', views.get_graves, name='get-graves'),
    # path('api/grave/<int:grave_id>/', views.get_grave_detail, name='get-grave-detail'),
    path('search/', views.search, name='search' ),
    path('product/<int:pk>', views.product, name='product' ),
    path('category/<str:foo>', views.category, name='category' ),

    path('qabristonmap/<int:pk>/', views.qabristonmap_view, name='qabristonmap'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)