from django.urls import include, path
from .views.items import ItemsView
from .views.items import ItemView

urlpatterns = [
    path('items/', ItemsView.as_view(), name='items'),
    path('items/<int:pk>', ItemView.as_view(), name='item'),

]