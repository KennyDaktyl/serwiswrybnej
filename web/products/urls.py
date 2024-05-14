from django.urls import path

from .views import ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    # path("<int:pk>/", views.ProductDetailView.as_view(), name="product-detail"),
]