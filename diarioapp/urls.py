from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.fazer_login,name='login'),
    path('logout',views.fazer_logout,name='logout'),
    path('escrever',views.escrever_diario,name='escrever'),
    path('detalhes',views.detalhes_usuario,name='detalhes'),
    path('editar/<id>/',views.editar_diario,name='editar-diario'),
    path('excluir/<int:id>',views.excluir_diario,name='excluir'),
]