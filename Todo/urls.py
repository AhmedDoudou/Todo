from django.urls import path
from .views import Todo_list, Todo_detail, Todo_create, Todo_update, Todo_delete

app_name = 'todos'

urlpatterns = [
    path('', Todo_list),
    path('create/', Todo_create),
    path('<id>/', Todo_detail),
    path('<id>/update/', Todo_update),
    path('<id>/delete/', Todo_delete)
]
