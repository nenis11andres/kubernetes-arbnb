from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from alojamientos_app.views import nuevo_alojamiento, mis_alojamientos, editar_alojamiento, ver_alquileres, mis_alquileres, nuevo_alquiler, comentar_alquiler
from usuarios_app.views import salir, registro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salir/', salir, name="salir"),
    path('mis_alojamientos/', mis_alojamientos, name='mis_alojamientos'),
    path('mis_alquileres/', mis_alquileres, name='mis_alquileres'),
    path('alquiler/nuevo/', nuevo_alquiler, name='nuevo_alquiler'),
    path('alquiler/<int:alquiler_id>/comentar/', comentar_alquiler, name='comentar_alquiler'),

    path('registro/', registro, name='registro'),
    path('alojamiento/<int:alojamiento_id>/editar/', editar_alojamiento, name='editar_alojamiento'),
    path('alojamiento/<int:alojamiento_id>/alquileres/', ver_alquileres, name='ver_alquileres'),
    path('alojamiento/nuevo/', nuevo_alojamiento, name='nuevo_alojamiento'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]