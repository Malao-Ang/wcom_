from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index,name = 'dashboard-index'),
    path('staff/',views.staff,name ='dashboard-staff'),
    path('expenses/',views.expenses,name ='dashboard-expenses'),
    path('income/',views.income,name ='dashboard-income'),
    path('income/delete/<int:ind>/',views.Income_delete,name ='dashboard-income-delete'),
    path('sale/',views.sale,name ='dashboard-sale'),
]

