from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetPayloadView),
    path('<int:pk>/', views.GetPayloadView),
    path('create/', views.CreatePayload),
    path('<int:pk>/update', views.UpdatePayload),
    path('<int:pk>/delete', views.DeletePayload),
]
