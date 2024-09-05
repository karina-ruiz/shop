from django.urls import path
from .view import ProductFormView

urlpatterns = [
    path('agregar/', ProductFormView.as_view(), name="add_product"),

]