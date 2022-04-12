from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index,name = 'dashboard-index'),
    path('staff/',views.staff,name ='dashboard-staff'),
    path('expenses/',views.expenses,name ='dashboard-expenses'),
    path('expenses/delete/<int:ind>/',views.expenses_delete,name ='dashboard-expenses-delete'),
    path('expenses/update/<int:ind>/',views.expenses_update,name ='dashboard-expenses-update'),
    path('income/',views.income,name ='dashboard-income'),
    path('income/delete/<int:ind>/',views.Income_delete,name ='dashboard-income-delete'),
    path('income/update/<int:ind>/',views.Income_update,name ='dashboard-income-update'),
    path('sale/',views.sale_static,name ='dashboard-sale'),
    path('sale/delete/<int:ind>/',views.sale_static_delete,name ='dashboard-sale-delete'),
    path('sale/update/<int:ind>/',views.sale_static_update,name ='dashboard-sale-update'),
]

