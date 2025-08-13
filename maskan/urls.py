from django.urls import path, include
from .import views



urlpatterns = [
    # Ro'yxatdan o'tish jarayoni

    
    path('api/bot-register/', views.api_bot_register, name='api_bot_register'),
    path('api/bot-start/', views.api_bot_start, name='api_bot_start'),


    path('login/', views.login_user, name='login'),
    path('', views.home, name='home' ),
    path('/one-to-one/', include('one_to_one.urls')),
    path('product/<int:pk>', views.product, name='product' ),
    path('category/<str:foo>', views.category, name='category' ),
    path('qabristonmap/<int:pk>/', views.qabristonmap_view, name='qabristonmap'),
    path('qabristonmap/<int:pk>/search/', views.qabristonmap_search_page, name='qabristonmap_search'),
    path('qabristonmap/<int:pk>/search/ajax/', views.qabristonmap_search_ajax, name='qabristonmap_search_ajax'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)