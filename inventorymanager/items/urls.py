from django.urls import include, path
from .views.items import ItemsView
from .views.items import ItemView
from .views.shipments import ShipmentsView
from .views.items import ItemUndeleteView
from .views.items import DeletedItemsView

urlpatterns = [
    path('items/', ItemsView.as_view(), name='items'),
    path('items/<int:pk>', ItemView.as_view(), name='item'),
    path('items/undelete/<int:pk>', ItemUndeleteView.as_view(), name='undelete'),
    path('items/deleted/', DeletedItemsView.as_view(), name='viewdeleted')

]