from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page,name='add'),
    path('snippets/list', views.snippets_list,name= 'list'),
    path('snippets/<int:value>/', views.snippets_page,name= 'list-page'),
    path('snippets/create',views.snippets_create,name = 'snippets-create'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
