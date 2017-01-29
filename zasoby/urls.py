"""zasoby URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from store.views import StoreListView, CreateProduct, ListOwners, EditOwner, CreateOwner, DeleteOwner, DetailProductView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'store/$', StoreListView.as_view(), name = 'store-list',),
    url(r'store/new$', CreateProduct.as_view(), name = 'add-product',),
    url(r'store/list-owner$', ListOwners.as_view(), name = 'list-owner',),
    url(r'store/add-owner$', CreateOwner.as_view(), name = 'add-owner',),
    url(r'store/edit(?P<pk>\d+)/$', EditOwner.as_view(), name = 'edit-owner',),
    url(r'store/delete(?P<pk>\d+)/$', DeleteOwner.as_view(), name = 'delete-owner',),
    url(r'^store/product-edit(?P<pk>[-\w]+)/$', DetailProductView.as_view(), name='product-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
