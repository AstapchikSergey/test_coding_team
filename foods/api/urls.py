from django.urls import include, path

urlpatterns = [
    path('v1/', include('foods.api.v1.urls')),
]
