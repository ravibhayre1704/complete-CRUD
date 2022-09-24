from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='form'),
    path('login/',views.login, name='login_form'),
    path('welcome/',views.welcome, name='welcome'),
    path('table/',views.table, name='data'),
    path('form_data/',views.form_data,name='reform'),
    path('login_data/',views.Login_form,name='form'),
    path('data/',views.data,name='alldata'),
    path('delete_user/',views.delete_user),
    path('update_view/<int:uid>/',views.update_view),
    path('update_form_data/',views.update_form_data)


]
