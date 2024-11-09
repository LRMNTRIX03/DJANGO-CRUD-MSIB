from django.urls import path, include
from . import views

app_name = 'app1'

urlpatterns = [
    path('inputBarang', views.inputBarang_view, name='inputbarang'),
    path('tampilBarang', views.tampilBarang_view, name='showbarang'),
    path('editBarang/<int:id>', views.editBarang_view, name='editbarang'),
    path('deleteBarang/<int:id>', views.DeleteBarang_view, name='deletebarang'),
    
    
]